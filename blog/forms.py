from django import forms
from .models import Comment
from django.utils.translation import gettext_lazy as _


class CommentForm(forms.ModelForm):
    author_fullname = forms.CharField(label='',
                                      required=True,
                                      widget=forms.TextInput(
                                        attrs={
                                            'placeholder': _('Name')
                                        }
                                      ))
    comment = forms.CharField(label='',
                              widget=forms.Textarea(
                                attrs={
                                    'placeholder': _('Message')
                                }
                              ))

    class Meta:
        model = Comment
        fields = ('author_fullname', 'comment')
