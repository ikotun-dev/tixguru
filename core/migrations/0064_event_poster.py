# Generated by Django 4.0.4 on 2023-01-01 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0063_alter_media_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='poster',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
