# Generated by Django 3.2.4 on 2021-06-14 08:08

import core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aids', '0135_add_special_status_audience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aid',
            name='targeted_audiences',
            field=core.fields.ChoiceArrayField(base_field=models.CharField(choices=[('commune', 'Communes'), ('epci', 'Audience EPCI'), ('department', 'Departments'), ('region', 'Regions'), ('special', 'Special status for outre-mer'), ('association', 'Associations'), ('private_sector', 'Private sector'), ('public_cies', 'Local public companies'), ('public_org', 'Public organization'), ('researcher', 'Research'), ('private_person', 'Individuals'), ('farmer', 'Farmers')], max_length=32), blank=True, null=True, size=None, verbose_name='Targeted audiences'),
        ),
    ]