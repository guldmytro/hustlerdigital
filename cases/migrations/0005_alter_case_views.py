# Generated by Django 4.1.2 on 2022-10-23 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0004_case_color_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='views',
            field=models.CharField(max_length=20, verbose_name='Views'),
        ),
    ]
