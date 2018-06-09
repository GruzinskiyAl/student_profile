# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-08 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject_controller', '0017_auto_20180608_1008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subjectofunivgroup',
            options={'ordering': ['start_semester'], 'verbose_name': 'Предмет группы', 'verbose_name_plural': 'Предметы группы'},
        ),
        migrations.RenameField(
            model_name='subjectofunivgroup',
            old_name='semester',
            new_name='semester_quantity',
        ),
        migrations.AddField(
            model_name='subjectofunivgroup',
            name='start_semester',
            field=models.FloatField(choices=[(0.5, 0.5), (1.0, 1.0), (1.5, 1.5), (2.0, 2.0), (2.5, 2.5), (3.0, 3.0), (3.5, 3.5), (4.0, 4.0)], default=1.0),
        ),
    ]