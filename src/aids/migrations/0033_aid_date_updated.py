# Generated by Django 2.1.1 on 2018-09-27 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aids', '0032_auto_20180927_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='aid',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Date updated'),
        ),
    ]
