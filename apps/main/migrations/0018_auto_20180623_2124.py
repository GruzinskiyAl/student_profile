# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-23 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20180623_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='t_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер телефона'),
        ),
    ]