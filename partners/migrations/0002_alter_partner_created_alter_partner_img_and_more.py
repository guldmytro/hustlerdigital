# Generated by Django 4.1.2 on 2022-10-16 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='img',
            field=models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='link',
            field=models.URLField(verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Title'),
        ),
    ]
