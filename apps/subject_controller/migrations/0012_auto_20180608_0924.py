# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-08 09:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject_controller', '0011_auto_20180608_0919'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubjectMark',
            new_name='ExamSubjectMark',
        ),
    ]