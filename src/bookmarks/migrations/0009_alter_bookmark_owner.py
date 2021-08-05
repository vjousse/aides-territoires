# Generated by Django 3.2.4 on 2021-08-03 22:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookmarks', '0008_cleanup_choices_translations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmarks', to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
    ]