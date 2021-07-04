# Generated by Django 3.2.4 on 2021-07-01 14:28

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perimeter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Nom')),
                ('insee', models.CharField(max_length=16, verbose_name='code INSEE')),
                ('wikipedia', models.CharField(max_length=255, verbose_name='wikipedia')),
                ('poly', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
    ]
