# Generated by Django 3.0.2 on 2020-06-01 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_auto_20200531_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='simple',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='simple',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
