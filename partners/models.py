from django.db import models
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _


class Partner(models.Model):
    title = models.CharField(max_length=30, verbose_name=_('Title'))
    img = models.ImageField(upload_to='images/%Y/%m/%d/',
                            verbose_name=_('Image'))
    link = models.URLField(verbose_name=_('Link'))
    created = models.DateTimeField(auto_now_add=True, db_index=True,
                                   verbose_name=_('Created'))

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Partner')
        verbose_name_plural = _('Partners')

    def __str__(self):
        return self.title

    @admin.display(description=_('Image'))
    def img_tag(self):
        tag = f'<img src="{self.img.url}" width="50" height="50" style="object-fit:contain">'
        return mark_safe(tag)
