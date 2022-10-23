from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import AdvUser, Post, Comment


@admin.register(AdvUser)
class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fields = (
        ('username', 'email'),
        ('photo', 'profession'),
        ('first_name', 'last_name'),
        ('is_staff', 'is_superuser'),
        'groups', 'user_permissions',
        ('last_login', 'date_joined')
    )
    readonly_fields = ('last_login', 'date_joined')


class CommentInline(admin.StackedInline):
    model = Comment


@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    list_display = ('__str__', 'created')
    search_fields = ('title', 'content')
    list_filter = ('created',)
    inlines = [CommentInline]
