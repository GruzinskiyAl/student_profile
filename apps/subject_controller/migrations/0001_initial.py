# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-11 18:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_hall', models.CharField(max_length=50, verbose_name='Аудитория')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('descriprion', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('teacer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectAdditionalMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_material', models.TextField(blank=True, null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject_controller.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectLab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_url', models.URLField(blank=True, null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject_controller.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectLecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_url', models.URLField(blank=True, null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject_controller.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectLiterature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('literature', models.TextField(blank=True, null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject_controller.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectOfUnivGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.UnivGroup')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject_controller.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='WeekSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')], default=1, max_length=15)),
                ('lesson_num', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], default=1, max_length=2)),
                ('lecture_hall', models.CharField(max_length=50, null=True, verbose_name='Аудитория')),
                ('subject_denumerator', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='znam_subject', to='subject_controller.SubjectOfUnivGroup')),
                ('subject_numerator', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chisl_subject', to='subject_controller.SubjectOfUnivGroup')),
                ('univ_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.UnivGroup')),
            ],
        ),
        migrations.AddField(
            model_name='groupexam',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject_controller.Subject'),
        ),
        migrations.AddField(
            model_name='groupexam',
            name='univ_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.UnivGroup'),
        ),
    ]
