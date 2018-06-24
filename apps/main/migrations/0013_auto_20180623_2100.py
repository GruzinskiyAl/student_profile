# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-23 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20180623_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='academic_degree',
            field=models.CharField(default='', max_length=256, verbose_name='Ученая степень'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='academic_rank',
            field=models.CharField(default='', max_length=256, verbose_name='Ученое звание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='other_position',
            field=models.CharField(default='', max_length=256, verbose_name='Другие должности'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='room',
            field=models.CharField(default='', max_length=10, verbose_name='Ученая степень'),
            preserve_default=False,
        ),
    ]
