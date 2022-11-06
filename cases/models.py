from django.db import models
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Case(TranslatableModel):
    COLOR_CHOICES = (
        ('yellow', 'yellow'),
        ('blue', 'blue'),
        ('mint', 'mint'),
        ('red', 'red'),
        ('light-blue', 'light-blue'),
        ('orange', 'orange'),
        ('pink', 'pink'),
        ('light', 'light'),
        ('green', 'green')
    )
    color_theme = models.CharField(verbose_name=_('Color theme'),
                                   choices=COLOR_CHOICES, default='yellow',
                                   max_length=20)
    translations = TranslatedFields(
        title=models.CharField(max_length=30, verbose_name=_('Title')),
        description=models.TextField(max_length=200, verbose_name=_('Description'),
                                     blank=True, null=True),
        footer_text=models.TextField(verbose_name=_('Footer text'), blank=True,
                                     null=True, max_length=200)
    )
    img = models.ImageField(upload_to='images/%Y/%m/%d/',
                            verbose_name=_('Image'))
    influencers = models.CharField(verbose_name=_('Influencers'), max_length=20)
    views = models.CharField(verbose_name=_('Views'), max_length=20)
    created = models.DateTimeField(auto_now_add=True, db_index=True,
                                   verbose_name=_('Created'))

    class Meta:
        ordering = ('created',)
        verbose_name = _('Case')
        verbose_name_plural = _('Cases')

    def __str__(self):
        return self.title

    @admin.display(description=_('Image'))
    def img_tag(self):
        tag = f'<img src="{self.img.url}" width="50" height="50" style="object-fit:contain">'
        return mark_safe(tag)
