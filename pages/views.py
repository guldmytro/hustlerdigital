from django.shortcuts import render
from django.http import JsonResponse
from cases.models import Case
from partners.models import Partner
from .forms import ContactForm
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


def home_view(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            cd = contact_form.cleaned_data
            subject = render_to_string('email/contact_letter_subject.txt')
            body_text = render_to_string('email/contact_letter_body.txt', {
                'name': cd['name'],
                'email': cd['email'],
                'link': cd['link'],
                'budget': cd['budget'],
                'message': cd['message']
            })
            send_mail(subject=subject, message=body_text, from_email=settings.EMAIL_HOST_USER, recipient_list=settings.MAIL_RECIPIENTS)
            return JsonResponse({'status': 'ok',
                'message': 'the form is valid'
            })
        else:
            return JsonResponse({'status': 'bad',
                'message': 'the form is not valid'
            })
    else:
        contact_form = ContactForm()
    cases = Case.objects.all()
    partners = Partner.objects.all()
    return render(request, 'pages/home.html', {
        'cases': cases,
        'partners': partners,
        'contact_form': contact_form,
    })
