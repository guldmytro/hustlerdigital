from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Post
from django.views.decorators.http import require_POST
from .forms import CommentForm


def blog_list(request):
    latest_posts = Post.objects.defer('content_ru', 'content_en', 'content_ua').all()[:4]
    other_posts = Post.objects.defer('content_ru', 'content_en', 'content_ua').all()[4:8]
    return render(request, 'blog/list.html', {
        'latest_posts': latest_posts,
        'other_posts': other_posts,
        'section': 'blog',
    })


@require_POST
def blog_detail(request, pk):
    if request.user.is_authenticated:
        comment_form = CommentForm(
            initial={'author_fullname': 'Зарегистрированый пользователь'})
    else:
        comment_form = CommentForm()
    post = Post.objects.prefetch_related('comments').get(id=pk)
    return render(request, 'blog/detail.html', {
        'post': post,
        'comment_form': comment_form,
    })


@require_POST
def blog_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        if request.user.is_authenticated:
            comment.author = request.user
        comment.save()
        return render(request, 'blog/comment.html', {
            'comment': comment
        }, status=200)
    return render(request, 'blog/comment-empty.html', {}, status=500)


@require_POST
def add_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.likes = post.likes + 1
    post.save()
    return JsonResponse({'likes': post.likes})


@require_POST
def delete_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.likes > 0:
        post.likes = post.likes - 1
        post.save()
    return JsonResponse({'likes': post.likes})
