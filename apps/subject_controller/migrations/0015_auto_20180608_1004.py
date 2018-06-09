# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-08 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject_controller', '0014_auto_20180608_0940'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentsubjectmark',
            options={'verbose_name': 'Оценка', 'verbose_name_plural': 'Оценки'},
        ),
        migrations.AlterField(
            model_name='examsubjectmark',
            name='simple_mark',
            field=models.IntegerField(choices=[(0.5, 0.5), (1.0, 1.0), (1.5, 1.5), (2.0, 2.0), (2.5, 2.5), (3.0, 3.0), (3.5, 3.5), (4.0, 4.0)], default=5),
        ),
        migrations.AlterField(
            model_name='studentsubjectmark',
            name='simple_mark',
            field=models.IntegerField(choices=[(0.5, 0.5), (1.0, 1.0), (1.5, 1.5), (2.0, 2.0), (2.5, 2.5), (3.0, 3.0), (3.5, 3.5), (4.0, 4.0)], default=5),
        ),
    ]