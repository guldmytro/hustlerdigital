from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    slug = models.SlugField(max_length=50, verbose_name=_('Slug'))

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return self.name


class Youtuber(models.Model):
    tags = models.ManyToManyField(Tag, verbose_name=_('Tags'))
    youtube_url = models.URLField(verbose_name=_('Youtube Link'), unique=True)
    title = models.CharField(max_length=300, verbose_name=_('Title'),
                             blank=True, null=True)
    thumb_url = models.URLField(verbose_name=_('Logo link'), blank=True,
                                null=True)
    subscribers = models.CharField(verbose_name=_('Subscribers'), blank=True,
                                   null=True, max_length=20)
    views = models.PositiveBigIntegerField(verbose_name=_('Views'),
                                           blank=True, null=True)
    last_video = models.CharField(verbose_name=_('Last video'), blank=True,
                                  null=True, max_length=20)

    class Meta:
        ordering = ('-title',)
        verbose_name = _('Youtuber')
        verbose_name_plural = _('Youtubers')

    def __str__(self):
        return self.youtube_url


class Instagram(models.Model):
    tags = models.ManyToManyField(Tag, verbose_name=_('Tags'))
    instagram_url = models.URLField(verbose_name=_('Instagram Link'),
                                    unique=True)
    title = models.CharField(max_length=300, verbose_name=_('Title'),
                             blank=True, null=True)
    thumb = models.ImageField(upload_to='images/%Y/%m/%d/',
                              verbose_name=_('Logo link'), blank=True,
                              null=True)
    subscribers = models.CharField(verbose_name=_('Subscribers'), blank=True,
                                   null=True, max_length=20)
    involvement = models.CharField(verbose_name=_('Involvement'), blank=True,
                                   null=True, max_length=20)

    class Meta:
        ordering = ('-title',)
        verbose_name = _('Instagram')
        verbose_name_plural = _('Instagram')

    def __str__(self):
        return self.instagram_url


class Twich(models.Model):
    tags = models.ManyToManyField(Tag, verbose_name=_('Tags'))
    twich_url = models.URLField(verbose_name=_('Twich Link'),
                                unique=True)
    title = models.CharField(max_length=300, verbose_name=_('Title'),
                             blank=True, null=True)
    thumb_url = models.URLField(verbose_name=_('Logo link'), blank=True,
                                null=True)
    subscribers = models.CharField(verbose_name=_('Subscribers'), blank=True,
                                   null=True, max_length=20)
    average_online = models.CharField(verbose_name=_('Average online'),
                                      blank=True, null=True, max_length=20)
    last_stream = models.CharField(verbose_name=_('Last stream'), blank=True,
                                   null=True, max_length=20)

    class Meta:
        ordering = ('-title',)
        verbose_name = _('Twich')
        verbose_name_plural = _('Twich')

    def __str__(self):
        return self.twich_url
