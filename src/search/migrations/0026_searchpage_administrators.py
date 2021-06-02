# Generated by Django 3.2.2 on 2021-05-25 20:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('search', '0025_searchpage_highlighted_aids'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchpage',
            name='administrators',
            field=models.ManyToManyField(blank=True, related_name='administrator_of_search_pages', to=settings.AUTH_USER_MODEL, verbose_name='Administrators'),
        ),
    ]
