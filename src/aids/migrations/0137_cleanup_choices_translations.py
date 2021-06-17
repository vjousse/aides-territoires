# Generated by Django 3.2.4 on 2021-06-14 20:48

import core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aids', '0136_alter_aid_targeted_audiences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aid',
            name='aid_types',
            field=core.fields.ChoiceArrayField(base_field=models.CharField(choices=[('grant', 'Subvention'), ('loan', 'Prêt'), ('recoverable_advance', 'Avance récupérable'), ('technical', 'Aides en ingénierie'), ('financial', 'Aides financières'), ('legal', 'Ingénierie juridique / administrative'), ('other', 'Autre')], max_length=32), blank=True, help_text='Specify the aid type or types.', null=True, size=None, verbose_name='Aid types'),
        ),
        migrations.AlterField(
            model_name='aid',
            name='destinations',
            field=core.fields.ChoiceArrayField(base_field=models.CharField(choices=[('supply', 'Dépenses de fonctionnement'), ('investment', "Dépenses d'investissement")], max_length=32), blank=True, null=True, size=None, verbose_name='Destinations'),
        ),
        migrations.AlterField(
            model_name='aid',
            name='import_share_licence',
            field=models.CharField(blank=True, choices=[('unknown', 'Inconnu'), ('openlicence20', 'Licence ouverte 2.0')], max_length=50, verbose_name='Under which license was this aid shared?'),
        ),
        migrations.AlterField(
            model_name='aid',
            name='mobilization_steps',
            field=core.fields.ChoiceArrayField(base_field=models.CharField(choices=[('preop', 'Réflexion / conception'), ('op', 'Mise en œuvre / réalisation'), ('postop', 'Usage / valorisation')], default='preop', max_length=32), blank=True, null=True, size=None, verbose_name='Mobilization step'),
        ),
        migrations.AlterField(
            model_name='aid',
            name='recurrence',
            field=models.CharField(blank=True, choices=[('oneoff', 'Ponctuelle'), ('ongoing', 'Permanente'), ('recurring', 'Récurrente')], help_text='Is this a one-off aid, is it recurring or ongoing?', max_length=16, verbose_name='Recurrence'),
        ),
        migrations.AlterField(
            model_name='aid',
            name='targeted_audiences',
            field=core.fields.ChoiceArrayField(base_field=models.CharField(choices=[('commune', 'Communes'), ('epci', 'EPCI à fiscalité propre'), ('department', 'Départements'), ('region', 'Régions'), ('special', "Collectivités d'outre-mer à statuts particuliers"), ('association', 'Associations'), ('private_sector', 'Entreprises privées'), ('public_cies', 'Entreprises publiques locales (Sem, Spl, SemOp)'), ('public_org', 'Établissement public'), ('researcher', 'Recherche'), ('private_person', 'Particuliers'), ('farmer', 'Agriculteurs')], max_length=32), blank=True, null=True, size=None, verbose_name='Targeted audiences'),
        ),
        migrations.AlterField(
            model_name='aidfinancer',
            name='order',
            field=models.PositiveIntegerField(default=1, verbose_name='Trier par'),
        ),
        migrations.AlterField(
            model_name='aidinstructor',
            name='order',
            field=models.PositiveIntegerField(default=1, verbose_name='Trier par'),
        ),
    ]