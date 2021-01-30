# Generated by Django 3.1.5 on 2021-01-30 14:39

import core.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_auto_20200217_1136'),
        ('geofr', '0030_perimeter_is_visible_to_users_init'),
        ('stats', '0004_event_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='AidSearchEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('targeted_audiences', core.fields.ChoiceArrayField(base_field=models.CharField(choices=[('commune', 'Communes'), ('epci', 'Audience EPCI'), ('department', 'Departments'), ('region', 'Regions'), ('association', 'Associations'), ('private_sector', 'Private sector'), ('public_cies', 'Local public companies'), ('public_org', 'Public organization'), ('researcher', 'Research'), ('private_person', 'Individuals'), ('farmer', 'Farmers'), ('other', 'Other')], max_length=32), blank=True, null=True, size=None, verbose_name='Targeted audiences')),
                ('raw_search', models.JSONField(blank=True, verbose_name='Raw search query')),
                ('results_count', models.PositiveIntegerField(verbose_name='Results count')),
                ('source', models.CharField(default='', max_length=256, verbose_name='Source')),
                ('fields_populated', models.BooleanField(default=False, verbose_name='Fields populated?')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date created')),
                ('categories', models.ManyToManyField(blank=True, related_name='aid_search_events', to='categories.Category', verbose_name='Categories')),
                ('perimeter', models.ForeignKey(blank=True, help_text='What is the searched perimeter?', null=True, on_delete=django.db.models.deletion.PROTECT, to='geofr.perimeter', verbose_name='Perimeter')),
                ('themes', models.ManyToManyField(blank=True, related_name='aid_search_events', to='categories.Theme', verbose_name='Themes')),
            ],
            options={
                'verbose_name': 'Aid Search Event',
                'verbose_name_plural': 'Aid Search Events',
            },
        ),
    ]
