# Generated by Django 4.0.4 on 2022-12-23 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_customerinfo_ticket_ticket_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='email',
        ),
    ]
