# Generated by Django 4.0.4 on 2022-12-23 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_alter_event_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='slug',
        ),
    ]
