# Generated by Django 3.2.4 on 2021-06-14 08:08

import core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0021_promotiondisplayevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aidsearchevent',
            name='targeted_audiences',
            field=core.fields.ChoiceArrayField(base_field=models.CharField(choices=[('commune', 'Communes'), ('epci', 'Audience EPCI'), ('department', 'Departments'), ('region', 'Regions'), ('special', 'Special status for outre-mer'), ('association', 'Associations'), ('private_sector', 'Private sector'), ('public_cies', 'Local public companies'), ('public_org', 'Public organization'), ('researcher', 'Research'), ('private_person', 'Individuals'), ('farmer', 'Farmers')], max_length=32), blank=True, null=True, size=None, verbose_name='Targeted audiences'),
        ),
        migrations.AlterField(
            model_name='aidviewevent',
            name='targeted_audiences',
            field=core.fields.ChoiceArrayField(base_field=models.CharField(choices=[('commune', 'Communes'), ('epci', 'Audience EPCI'), ('department', 'Departments'), ('region', 'Regions'), ('special', 'Special status for outre-mer'), ('association', 'Associations'), ('private_sector', 'Private sector'), ('public_cies', 'Local public companies'), ('public_org', 'Public organization'), ('researcher', 'Research'), ('private_person', 'Individuals'), ('farmer', 'Farmers')], max_length=32), blank=True, null=True, size=None, verbose_name='Targeted audiences'),
        ),
    ]
