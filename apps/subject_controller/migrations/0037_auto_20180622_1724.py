# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-22 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject_controller', '0036_auto_20180622_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectlecture',
            name='name',
            field=models.TextField(default='Лекция'),
        ),
    ]
