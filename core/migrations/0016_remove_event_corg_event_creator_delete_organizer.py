# Generated by Django 4.0.4 on 2022-11-24 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0015_rename_creator_event_corg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='corg',
        ),
        migrations.AddField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Organizer',
        ),
    ]
