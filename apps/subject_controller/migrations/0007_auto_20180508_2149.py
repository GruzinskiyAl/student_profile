# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-08 21:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('subject_controller', '0006_auto_20180508_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupexam',
            name='exam_datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 8, 21, 49, 55, 581932, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subjectmark',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 5, 8, 21, 49, 55, 582754, tzinfo=utc)),
        ),
    ]