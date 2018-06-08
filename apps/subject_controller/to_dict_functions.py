# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib import auth

from apps.main.models import *
from .models import *


DAY_STATUS_CHOICES = (
    ('Monday', u'Понедельник'),
    ('Tuesday', u'Вторник'),
    ('Wednesday', u'Среда'),
    ('Thursday', u'Четверг'),
    ('Friday', u'Пятница'),
    ('Sunday', u'Суббота')
)


def schedule_for_template(schedule_queryset):
    schedule_list = []
    for en_day, ru_day in DAY_STATUS_CHOICES:
        schedule_dict = {}
        num_dict = {}
        for lesson in range(1, 9):
            try:
                subject_num = ''
                subject_denom = ''
                schedule_obj = schedule_queryset.get(day=en_day, lesson_num=lesson)
                if schedule_obj.subject_numerator:
                    subject_num = 'Чс: ' + schedule_obj.subject_numerator.subject.name
                    subject_num += ' ' + str(schedule_obj.subject_numerator.subject.teacher.name_initials_string())
                    subject_num += ' ' + str(schedule_obj.lecture_hall_numerator)
                if schedule_obj.subject_denominator:
                    subject_denom = subject_denom + ' Зн: ' + schedule_obj.subject_denominator.subject.name
                    subject_denom += ' ' + str(schedule_obj.subject_denominator.subject.teacher.name_initials_string())
                    subject_denom += ' ' + str(schedule_obj.lecture_hall_denominator)
                num_dict[lesson] = {'subject_num': subject_num,
                                    'subject_denom': subject_denom}
            except WeekSchedule.DoesNotExist:
                num_dict[lesson] = ''
        schedule_dict[ru_day] = num_dict
        schedule_list.append(schedule_dict)
    return schedule_list


def subject_materials_for_template(group_subject_object):
    labs = SubjectLab.objects.filter(subject=group_subject_object)
    lectures = SubjectLecture.objects.filter(subject=group_subject_object)
    literature = SubjectLiterature.objects.filter(subject=group_subject_object)
    material = SubjectAdditionalMaterial.objects.filter(subject=group_subject_object)
    return labs, lectures, literature, material


def subject_list_with_marks(student):
    subjects = SubjectOfUnivGroup.objects.filter(group=student.univ_group)
    marks = ExamSubjectMark.objects.filter(student=student)
    subjects_with_marks = {}
    for subject in subjects:
        marks_list = ''
        for mark in marks.filter(subject=subject).values_list('full_mark'):
            marks_list += str(mark[0]) + ', '
        subjects_with_marks[subject] = marks_list
    return subjects_with_marks
