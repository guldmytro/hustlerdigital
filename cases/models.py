from django.db import models
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _


class Case(models.Model):
    title = models.CharField(max_length=30, verbose_name=_('Title'))
    img = models.ImageField(upload_to='images/%Y/%m/%d/',
                            verbose_name=_('Image'))
    budget = models.CharField(max_length=10, verbose_name=_('Budget'))
    area = models.CharField(max_length=10, verbose_name=_('Coverage'))
    service = models.TextField(max_length=200, verbose_name=_('Service'))
    geo = models.CharField(max_length=20, verbose_name=_('Geo'))
    created = models.DateTimeField(auto_now_add=True, db_index=True,
                                   verbose_name=_('Created'))

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Case')
        verbose_name_plural = _('Cases')

    def __str__(self):
        return self.title

    @admin.display(description=_('Image'))
    def img_tag(self):
        tag = f'<img src="{self.img.url}" width="50" height="50" style="object-fit:contain">'
        return mark_safe(tag)


