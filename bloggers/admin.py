from django.contrib import admin
from .models import Youtuber, Tag, Instagram, Twich


@admin.register(Youtuber)
class YoutuberAdmin(admin.ModelAdmin):
    list_display = ['youtube_url']


@admin.register(Instagram)
class InstagramAdmin(admin.ModelAdmin):
    list_display = ['instagram_url']


@admin.register(Twich)
class TwichAdmin(admin.ModelAdmin):
    list_display = ['twich_url']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
