from django.shortcuts import render
from .models import Youtuber, Tag, Instagram, Twich
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import TagsForm, SearchForm


def bloggers_list(request):
    tags_form = TagsForm(request.GET)
    search_form = SearchForm(request.GET)
    tags = Tag.objects.all()
    if request.GET.get('type') == 'instagram':
        object_list = Instagram.objects.all()
        post_type = 'instagram'
    elif request.GET.get('type') == 'twich':
        object_list = Twich.objects.all()
        post_type = 'twich'
    else:
        object_list = Youtuber.objects.all()
        post_type = 'youtube'

    # Filtering query
    if search_form.is_valid() and tags_form.is_valid():
        search_form_data = search_form.cleaned_data
        tags_form_data = tags_form.cleaned_data
        if search_form_data.get('search'):
            object_list = object_list.filter(title__icontains=search_form_data['search'])
        if tags_form_data.get('tag'):
            object_list = object_list.filter(tags__in=tags_form_data.get('tag'))

    paginator = Paginator(object_list, 12)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'bloggers/list.html', {
        'tags': tags,
        'posts': posts,
        'tags_form': tags_form,
        'search_form': search_form,
        'post_type': post_type,
        'section': 'bloggers',
    })
