# Generated by Django 4.0.4 on 2022-12-23 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_remove_review_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
