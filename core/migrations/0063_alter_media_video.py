# Generated by Django 4.0.4 on 2023-01-01 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0062_alter_media_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='video',
            field=models.FileField(default='pictures/video.mp4', upload_to='media'),
        ),
    ]
