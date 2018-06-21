# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-21 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject_controller', '0030_auto_20180621_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='examsubjectmark',
            name='semester',
            field=models.FloatField(choices=[(0.5, 0.5), (1.0, 1.0), (1.5, 1.5), (2.0, 2.0), (2.5, 2.5), (3.0, 3.0), (3.5, 3.5), (4.0, 4.0), (4.5, 4.5), (5.0, 5.0), (5.5, 5.5), (6.0, 6.0), (6.5, 6.5), (7.0, 7.0), (7.5, 7.5), (8.0, 8.0)], default=1.0, verbose_name='Семестр'),
        ),
        migrations.AlterField(
            model_name='studentsubjectmark',
            name='semester',
            field=models.FloatField(choices=[(0.5, 0.5), (1.0, 1.0), (1.5, 1.5), (2.0, 2.0), (2.5, 2.5), (3.0, 3.0), (3.5, 3.5), (4.0, 4.0), (4.5, 4.5), (5.0, 5.0), (5.5, 5.5), (6.0, 6.0), (6.5, 6.5), (7.0, 7.0), (7.5, 7.5), (8.0, 8.0)], default=1.0, verbose_name='Семестр'),
        ),
        migrations.AlterField(
            model_name='subjectofunivgroup',
            name='semester_quantity',
            field=models.FloatField(choices=[(0.5, 0.5), (1.0, 1.0), (1.5, 1.5), (2.0, 2.0), (2.5, 2.5), (3.0, 3.0), (3.5, 3.5), (4.0, 4.0), (4.5, 4.5), (5.0, 5.0), (5.5, 5.5), (6.0, 6.0), (6.5, 6.5), (7.0, 7.0), (7.5, 7.5), (8.0, 8.0)], default=1.0, verbose_name='Семестр окончания'),
        ),
        migrations.AlterField(
            model_name='subjectofunivgroup',
            name='start_semester',
            field=models.FloatField(choices=[(0.5, 0.5), (1.0, 1.0), (1.5, 1.5), (2.0, 2.0), (2.5, 2.5), (3.0, 3.0), (3.5, 3.5), (4.0, 4.0), (4.5, 4.5), (5.0, 5.0), (5.5, 5.5), (6.0, 6.0), (6.5, 6.5), (7.0, 7.0), (7.5, 7.5), (8.0, 8.0)], default=1.0, verbose_name='Начальный семестр'),
        ),
    ]
