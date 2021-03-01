# Generated by Django 3.1.6 on 2021-02-15 17:22

from django.db import migrations


def copy_data_from_event_table(apps, schema_editor):
    Aid = apps.get_model('aids', 'Aid')
    Event = apps.get_model('stats', 'Event')
    AidViewEvent = apps.get_model('stats', 'AidViewEvent')

    all_aids = Aid.objects.all()
    events = Event.objects.filter(category='aid', event='viewed')
    
    for event in events:
        try:
            aid = all_aids.get(slug=event.meta)
            AidViewEvent.objects.create(
                aid=aid,
                source=event.source,
                date_created=event.date_created)
            event.delete()
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0005_aidviewevent'),
    ]

    operations = [
        migrations.RunPython(copy_data_from_event_table)
    ]
