# Generated by Django 4.2.6 on 2023-10-09 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_comment',
            field=models.TextField(max_length=65535, null=True),
        ),
    ]
