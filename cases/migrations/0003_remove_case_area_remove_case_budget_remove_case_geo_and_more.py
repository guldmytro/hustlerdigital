# Generated by Django 4.1.2 on 2022-10-23 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_alter_case_area_alter_case_budget_alter_case_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='area',
        ),
        migrations.RemoveField(
            model_name='case',
            name='budget',
        ),
        migrations.RemoveField(
            model_name='case',
            name='geo',
        ),
        migrations.RemoveField(
            model_name='case',
            name='service',
        ),
        migrations.AddField(
            model_name='case',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='case',
            name='footer_text',
            field=models.TextField(blank=True, max_length='Footer text', null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='influencers',
            field=models.PositiveIntegerField(default=0, verbose_name='Influencers'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='case',
            name='views',
            field=models.PositiveBigIntegerField(default=0, verbose_name='Views'),
            preserve_default=False,
        ),
    ]
