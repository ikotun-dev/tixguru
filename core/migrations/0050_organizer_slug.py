# Generated by Django 4.0.4 on 2022-12-30 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_alter_event_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizer',
            name='slug',
            field=models.SlugField(default=0, max_length=500, unique=True),
            preserve_default=False,
        ),
    ]
