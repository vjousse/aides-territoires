# Generated by Django 3.2.4 on 2021-06-14 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataproviders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasource',
            name='import_licence',
            field=models.CharField(blank=True, choices=[('unknown', 'Inconnu'), ('openlicence20', 'Licence ouverte 2.0')], max_length=50, verbose_name='Under which license was this source imported?'),
        ),
    ]
