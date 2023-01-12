# Generated by Django 4.0.4 on 2022-12-05 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0020_alter_event_tickets_ava_alter_event_tickets_rem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Favourite',
            new_name='Bookmark',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='photo',
            new_name='poster',
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media')),
                ('video', models.FileField(null=True, upload_to='media')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.event')),
            ],
        ),
    ]
