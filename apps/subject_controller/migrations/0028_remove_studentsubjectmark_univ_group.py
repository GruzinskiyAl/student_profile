# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-09 15:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject_controller', '0027_auto_20180608_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentsubjectmark',
            name='univ_group',
        ),
    ]
