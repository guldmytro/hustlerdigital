from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    photo = models.ImageField(upload_to='images/%Y/%m/%d/',
                              verbose_name=_('Avatar'))
    profession = models.CharField(max_length=50, verbose_name=_('Profession'))

    class Meta(AbstractUser.Meta):
        pass


class Post(TranslatableModel):
    author = models.ForeignKey(AdvUser, related_name='posts',
                               on_delete=models.CASCADE)
    translations = TranslatedFields(
        title = models.CharField(max_length=100, verbose_name=_('Title')),
        excerpt = models.TextField(max_length=150, verbose_name=_('Short Excerpt')),
        content = models.TextField(verbose_name=_('Content'))
    )
    card_thumbnail = models.ImageField(upload_to='images/%Y/%m/%d/',
                                       verbose_name=_('Card Thumbnail'),
                                       help_text=_('Picture must be in \
                                                   png format with transparent\
                                                   background'))
    banner_thumbnail = models.ImageField(upload_to='images/%Y/%m/%d/',
                                         verbose_name=_('Banner Thumbnail'))
    popup_thumbnail = models.ImageField(upload_to='images/%Y/%m/%d/',
                                        verbose_name=_('Popup Thumbnail'))
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name=_('Created'), db_index=True)
    likes = models.PositiveIntegerField(verbose_name=_('Likes'),
                                        default=0)

    class Meta:
        ordering = ('-created',)
        verbose_name = _('New')
        verbose_name_plural = _('News')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(AdvUser, on_delete=models.CASCADE,
                               verbose_name=_('Author'), blank=True,
                               null=True)
    author_fullname = models.CharField(max_length=60, verbose_name=_('Author'),
                                       blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name=_('Post'))
    comment = models.TextField(max_length=500, verbose_name=_('Comment'))
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name=_('Created'))

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return f'#{self.pk}'
