# Generated by Django 4.0.4 on 2023-01-05 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0069_organizer_biz_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizer',
            name='bio',
            field=models.TextField(null=True),
        ),
    ]
