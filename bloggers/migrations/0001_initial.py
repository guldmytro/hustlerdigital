# Generated by Django 4.1.2 on 2022-10-21 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Youtuber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube_url', models.URLField(unique=True, verbose_name='Youtube Link')),
                ('title', models.CharField(blank=True, max_length=300, null=True, verbose_name='Title')),
                ('thumb_url', models.URLField(blank=True, null=True, verbose_name='Logo link')),
                ('subscribers', models.CharField(blank=True, max_length=20, null=True, verbose_name='Subscribers')),
                ('views', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Views')),
                ('last_video', models.CharField(blank=True, max_length=20, null=True, verbose_name='Last video')),
            ],
            options={
                'verbose_name': 'Youtuber',
                'verbose_name_plural': 'Youtubers',
            },
        ),
    ]