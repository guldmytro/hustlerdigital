# Generated by Django 4.1.2 on 2022-10-17 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='excerpt',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='content_en',
            field=models.TextField(default=0, verbose_name='Content EN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='content_ru',
            field=models.TextField(default=0, verbose_name='Content RU'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='content_ua',
            field=models.TextField(default=0, verbose_name='Content UA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='excerpt_en',
            field=models.TextField(default=0, max_length=150, verbose_name='Short Excerpt EN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='excerpt_ru',
            field=models.TextField(default=0, max_length=150, verbose_name='Short Excerpt RU'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='excerpt_ua',
            field=models.TextField(default=0, max_length=150, verbose_name='Short Excerpt UA'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(default=0, max_length=100, verbose_name='Title EN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(default=0, max_length=100, verbose_name='Title RU'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title_ua',
            field=models.CharField(default=0, max_length=100, verbose_name='Title UA'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(default=0, verbose_name='Likes'),
        ),
    ]
