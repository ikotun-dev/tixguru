# Generated by Django 4.0.4 on 2022-11-24 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_event_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='venue',
        ),
    ]
