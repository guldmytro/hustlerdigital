from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Case


@admin.register(Case)
class CaseAdmin(TranslatableAdmin):
    list_display = ['img_tag', 'title', 'color_theme']
    list_display_links = ['img_tag', 'title']
    list_editable = ['color_theme']
    search_fields = ['title']
