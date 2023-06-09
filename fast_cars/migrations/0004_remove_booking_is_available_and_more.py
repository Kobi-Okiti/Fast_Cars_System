# Generated by Django 4.1.7 on 2023-06-02 19:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fast_cars', '0003_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='is_available',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='rental_end_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='rental_start_date',
        ),
        migrations.AddField(
            model_name='booking',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
