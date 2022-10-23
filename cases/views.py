from django.shortcuts import render
from .models import Case


def cases_list(request):
    cases = Case.objects.all()
    return render(request, 'cases/list.html', {
        'cases': cases,
        'section': 'cases',
    })

