# Generated by Django 5.0.6 on 2024-06-20 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_booking_bid_alter_booking_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='bid',
        ),
    ]
