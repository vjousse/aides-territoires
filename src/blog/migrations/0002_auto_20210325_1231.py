# Generated by Django 3.1.7 on 2021-03-25 11:31

import core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='meta_description',
            field=models.TextField(blank=True, default='', help_text='This will be displayed in SERPs. Keep it under 120 characters.', max_length=256, verbose_name='Meta description'),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_title',
            field=models.CharField(blank=True, default='', help_text="This will be displayed in SERPs. Keep it under 60 characters. Leave empty and we will reuse the post's title.", max_length=180, verbose_name='Meta title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categorie',
            field=core.fields.ChoiceArrayField(base_field=models.CharField(choices=[('webinar', 'webinar'), ('newsletter', 'newsletter'), ('communication', 'communication'), ('team', 'team')], max_length=32), blank=True, null=True, size=None, verbose_name='categorie'),
        ),
    ]