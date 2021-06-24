# Generated by Django 3.2.4 on 2021-06-11 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_page_timestamps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='minisite',
            field=models.ForeignKey(blank=True, help_text='Optional, link this page to a minisite.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pages', to='search.searchpage', verbose_name='Minisite'),
        ),
    ]
