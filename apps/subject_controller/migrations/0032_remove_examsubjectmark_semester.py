# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-21 15:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject_controller', '0031_auto_20180621_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examsubjectmark',
            name='semester',
        ),
    ]