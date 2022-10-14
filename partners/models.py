from django.db import models
from django.contrib import admin
from django.utils.html import mark_safe


class Partner(models.Model):
    title = models.CharField(max_length=30)
    img = models.ImageField(upload_to='images/%Y/%m/%d/')
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'

    def __str__(self):
        return self.title

    @admin.display(description='Image')
    def img_tag(self):
        tag = f'<img src="{self.img.url}" width="50" height="50" style="object-fit:contain">'
        return mark_safe(tag)
