# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-08 14:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject_controller', '0026_auto_20180608_1434'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentsubjectmark',
            options={'ordering': ['semester'], 'verbose_name': 'Оценка', 'verbose_name_plural': 'Оценки'},
        ),
    ]
