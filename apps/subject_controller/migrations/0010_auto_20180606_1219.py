# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-06 12:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject_controller', '0009_auto_20180606_1157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subjectlab',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='subjectlecture',
            options={'ordering': ['pk']},
        ),
    ]