# Generated by Django 4.0.4 on 2022-12-23 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_alter_event_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='slug',
        ),
    ]
