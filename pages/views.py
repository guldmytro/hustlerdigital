from django.shortcuts import render
from cases.models import Case
from partners.models import Partner


def home_view(request):
    cases = Case.objects.all()
    partners = Partner.objects.all()
    return render(request, 'pages/home.html', {
        'cases': cases,
        'partners': partners,
    })
