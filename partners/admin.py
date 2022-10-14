from django.contrib import admin
from .models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['img_tag', 'title']
    list_display_links = ['img_tag', 'title']
    search_fields = ['title']
