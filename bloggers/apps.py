from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BloggersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bloggers'
    verbose_name = _('Bloggers')
