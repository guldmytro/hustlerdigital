from django import forms
from .models import Tag
from django.utils.translation import gettext_lazy as _


class TagsForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all().order_by('name'),
        widget=forms.CheckboxSelectMultiple,
        required=False)

    class Meta:
        model = Tag
        fields = ('tag',)


class SearchForm(forms.Form):
    TYPE_CHOICES = (
        ('youtube', 'youtube'),
        ('instagram', 'instagram'),
        ('twich', 'twich')
    )
    search = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={
        'type': 'search',
        'placeholder': _('Search'),
    }))
    type = forms.ChoiceField(label='', widget=forms.RadioSelect(),
                             choices=TYPE_CHOICES)
