# Generated by Django 2.1.7 on 2019-02-19 01:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190219_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 19, 1, 2, 54, 693488, tzinfo=utc)),
        ),
    ]
