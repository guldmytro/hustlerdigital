# Generated by Django 4.1.2 on 2022-10-23 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloggers', '0005_alter_twich_options_remove_instagram_thumb_url_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instagram',
            options={'ordering': ('-title',), 'verbose_name': 'Instagram', 'verbose_name_plural': 'Instagram'},
        ),
        migrations.AlterModelOptions(
            name='twich',
            options={'ordering': ('-title',), 'verbose_name': 'Twich', 'verbose_name_plural': 'Twich'},
        ),
        migrations.AlterModelOptions(
            name='youtuber',
            options={'ordering': ('-title',), 'verbose_name': 'Youtuber', 'verbose_name_plural': 'Youtubers'},
        ),
    ]