# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-09 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='birth_date',
            field=models.DateField(null=True),
        ),
    ]
