# Generated by Django 4.2.6 on 2023-10-09 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling_app', '0008_alter_event_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='participants',
        ),
        migrations.DeleteModel(
            name='EventParticipant',
        ),
    ]
