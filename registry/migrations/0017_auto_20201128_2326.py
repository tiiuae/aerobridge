# Generated by Django 3.1.3 on 2020-11-28 23:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0016_auto_20200115_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='is_registered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='authorization',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 28, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='operator',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 28, 0, 0, tzinfo=utc)),
        ),
    ]