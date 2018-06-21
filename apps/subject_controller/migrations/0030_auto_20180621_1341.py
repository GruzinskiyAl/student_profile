# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-21 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject_controller', '0029_teachermessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectofunivgroup',
            name='closing_date',
        ),
        migrations.AlterField(
            model_name='subjectofunivgroup',
            name='semester_quantity',
            field=models.FloatField(choices=[(0.5, 0.5), (1.0, 1.0), (1.5, 1.5), (2.0, 2.0), (2.5, 2.5), (3.0, 3.0), (3.5, 3.5), (4.0, 4.0)], default=1.0, verbose_name='Семестр окончания'),
        ),
    ]
