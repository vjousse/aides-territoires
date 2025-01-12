# Generated by Django 3.2.4 on 2021-08-06 13:49

import core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aids', '0145_auto_20210804_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aid',
            name='aid_types',
            field=core.fields.ChoiceArrayField(base_field=models.CharField(choices=[('grant', 'Subvention'), ('loan', 'Prêt'), ('recoverable_advance', 'Avance récupérable'), ('technical', 'Technique'), ('financial', 'Financière'), ('legal', 'Juridique / administrative'), ('other', 'Autre')], max_length=32), blank=True, help_text="Précisez le ou les types de l'aide.", null=True, size=None, verbose_name="Types d'aide"),
        ),
        migrations.AlterField(
            model_name='aid',
            name='targeted_audiences',
            field=core.fields.ChoiceArrayField(base_field=models.CharField(choices=[('commune', 'Communes'), ('epci', 'EPCI à fiscalité propre'), ('department', 'Départements'), ('region', 'Régions'), ('special', "Collectivités d'outre-mer à statuts particuliers"), ('association', 'Associations'), ('private_person', 'Particuliers'), ('farmer', 'Agriculteurs'), ('private_sector', 'Entreprises privées'), ('public_cies', 'Entreprises publiques locales (Sem, Spl, SemOp)'), ('public_org', "Établissements publics (écoles, bibliothèques…) / Services de l'État"), ('researcher', 'Recherche')], max_length=32), blank=True, null=True, size=None, verbose_name="Bénéficiaires de l'aide"),
        ),
    ]
