# Generated by Django 4.0.4 on 2022-12-23 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_alter_event_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default=1, max_length=500, unique=True),
            preserve_default=False,
        ),
    ]
