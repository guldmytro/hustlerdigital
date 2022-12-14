# Generated by Django 4.1.2 on 2022-10-23 14:16

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0008_delete_project_alter_case_footer_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='description',
        ),
        migrations.RemoveField(
            model_name='case',
            name='footer_text',
        ),
        migrations.RemoveField(
            model_name='case',
            name='title',
        ),
        migrations.CreateModel(
            name='CaseTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=30, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('footer_text', models.TextField(blank=True, max_length=200, null=True, verbose_name='Footer text')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='cases.case')),
            ],
            options={
                'verbose_name': 'Case Translation',
                'db_table': 'cases_case_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
    ]
