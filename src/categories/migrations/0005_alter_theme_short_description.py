# Generated by Django 3.2.2 on 2021-05-21 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_auto_20200217_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='Short description'),
        ),
    ]