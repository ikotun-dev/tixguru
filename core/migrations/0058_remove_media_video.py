# Generated by Django 4.0.4 on 2023-01-01 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_remove_media_photo_media_photos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='video',
        ),
    ]
