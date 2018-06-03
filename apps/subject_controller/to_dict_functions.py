# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib import auth
from apps.subject_controller.models import (SubjectOfUnivGroup, SubjectMark,
                                            WeekSchedule)
from apps.main.models import *

DAY_STATUS_CHOICES = (
    (1, u'Понедельник'),
    (2, u'Вторник'),
    (3, u'Среда'),
    (4, u'Четверг'),
    (5, u'Пятница'),
    (6, u'Суббота')
)


def schedule_for_template(schedule_queryset):
    schedule_list = []
    for num, day in DAY_STATUS_CHOICES:
        schedule_dict = {}
        num_dict = {}
        for lesson in range(1, 9):
            try:
                schedule_obj = schedule_queryset.get(day=num, lesson_num=lesson)
                if schedule_obj.subject_numerator:
                    subject = schedule_obj.subject_numerator.subject.name
                if schedule_obj.subject_denominator:
                    subject = subject +' / '+ schedule_obj.subject_denominator.subject.name
                num_dict[lesson] = {'subject': subject,
                                    'place_numerator': schedule_obj.lecture_hall_numerator,
                                    'place_denominator': schedule_obj.lecture_hall_denominator}
            except WeekSchedule.DoesNotExist:
                num_dict[lesson] = ''
        schedule_dict[day] = num_dict
        schedule_list.append(schedule_dict)
    return schedule_list
