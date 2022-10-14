from django.db import models
from django.contrib import admin
from django.utils.html import mark_safe


class Case(models.Model):
    title = models.CharField(max_length=30)
    img = models.ImageField(upload_to='images/%Y/%m/%d/')
    budget = models.CharField(max_length=10)
    area = models.CharField(max_length=10)
    service = models.TextField(max_length=200)
    geo = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Case'
        verbose_name_plural = 'Cases'

    def __str__(self):
        return self.title

    @admin.display(description='Image')
    def img_tag(self):
        tag = f'<img src="{self.img.url}" width="50" height="50" style="object-fit:contain">'
        return mark_safe(tag)


