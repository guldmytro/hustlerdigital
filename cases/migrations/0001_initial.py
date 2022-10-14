# Generated by Django 4.1.2 on 2022-10-13 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to='images/%Y/%m/%d/')),
                ('budget', models.CharField(max_length=10)),
                ('area', models.CharField(max_length=10)),
                ('service', models.TextField(max_length=200)),
                ('geo', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'verbose_name': 'Case',
                'verbose_name_plural': 'Cases',
                'ordering': ('-created',),
            },
        ),
    ]
