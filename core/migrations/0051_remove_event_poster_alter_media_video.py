# Generated by Django 4.0.4 on 2022-12-31 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_organizer_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='poster',
        ),
        migrations.AlterField(
            model_name='media',
            name='video',
            field=models.FileField(default='settings.MEDIA_ROOT/pictures/video.mp4', upload_to='media'),
        ),
    ]
