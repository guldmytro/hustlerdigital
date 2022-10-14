from django.contrib import admin
from .models import Case


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ['img_tag', 'title', 'budget', 'area', 'geo']
    list_display_links = ['img_tag', 'title']
    list_filter = ['geo']
    search_fields = ['title']
