# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-04 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject_controller', '0003_auto_20180604_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekschedule',
            name='lecture_hall_denominator',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Аудитория знам'),
        ),
        migrations.AlterField(
            model_name='weekschedule',
            name='lecture_hall_numerator',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Аудитория чис'),
        ),
    ]