# Generated by Django 4.0.4 on 2023-03-02 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0075_remove_bookmark_event_bookmark_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='video',
        ),
        migrations.RemoveField(
            model_name='organizer',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='organizer',
            name='poster',
        ),
    ]
