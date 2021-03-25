# Generated by Django 3.1.7 on 2021-03-05 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0009_aidsearchevent_populate_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aidsearchevent',
            name='source',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='Source'),
        ),
        migrations.AlterField(
            model_name='aidsearchevent',
            name='text',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='Text search'),
        ),
    ]