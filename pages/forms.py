from dataclasses import fields
from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(label=False, widget=forms.TextInput(
        attrs={
            'placeholder': _('Name')
        }
    ))
    email = forms.CharField(label=False, widget=forms.TextInput(
        attrs={
            'placeholder': _('E-mail')
        }
    ))
    link = forms.CharField(label=False, widget=forms.TextInput(
        attrs={
            'placeholder': _('Project link')
        }
    ))
    budget = forms.CharField(label=False, widget=forms.TextInput(
        attrs={
            'placeholder': _('Advertising budget')
        }
    ))
    message = forms.CharField(label=False, widget=forms.Textarea(
        attrs={
            'placeholder': _('Message'),
            'rows': 7,
            'cols': 10
        }
    ))

    class Meta:
        fields = '__all__'