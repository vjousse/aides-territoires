# Generated by Django 3.1.7 on 2021-03-02 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0007_aidsearchevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='aidsearchevent',
            name='text',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Text search'),
        )
    ]
