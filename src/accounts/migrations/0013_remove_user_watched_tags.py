# Generated by Django 3.2.4 on 2021-06-22 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_user_is_contributor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='watched_tags',
        ),
    ]