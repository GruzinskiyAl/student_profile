from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib import auth
from apps.subject_controller.models import (SubjectOfUnivGroup, SubjectMark,
                                            WeekSchedule)
from apps.main.models import *


class SubjectList(View):
    def get(self, request):
        try:
            student = Student.objects.get(user=request.user)
            subjects = SubjectOfUnivGroup.objects.filter(group=student.univ_group)
            marks = SubjectMark.objects.filter(student=student)
            subjects_with_mark = {}
            for subject in subjects:
                try:
                    subjects_with_mark[subject] = str(marks.get(subject=subject).full_mark)
                except SubjectMark.DoesNotExist:
                    subjects_with_mark[subject] = 'N/A'
            return render(request, 'subject_list.html', {'subjects_with_mark': subjects_with_mark, 'student': student})
        except Student.DoesNotExist:
            return HttpResponse('NO')


class SubjectDebtList(View):
    def get(self, request):
        try:
            student = Student.objects.get(user=request.user)
            group = student.univ_group
            marks = SubjectMark.objects.filter(student=student)
            subjects_marks = SubjectOfUnivGroup.objects.filter(subject__in=marks.values_list('subject'))
            subjects = SubjectOfUnivGroup.objects.exclude(pk__in=subjects_marks).filter(group=group)
            return render(request, 'debt.html', {'subjects': subjects})
        except Student.DoesNotExist:
            return HttpResponse('NO')


class StudentSchedule(View):

    def get(self, request):
        try:
            student = Student.objects.get(user=request.user)
            schedules = WeekSchedule.objects.filter(univ_group=student.univ_group)
            day_dict = {}
            for day in schedules.values_list('day'):
                num_dict = {}
                for lesson in range(1, 9):
                    try:
                        num_dict[lesson] = schedules.get(day=day, lesson_num=lesson)
                    except WeekSchedule.DoesNotExist:
                        num_dict[lesson] = ''
                day_dict[day] = num_dict
            return render(request, 'schedule.html', {'day_dict': day_dict, 'student': student})
        except (Student.DoesNotExist, ):
            return HttpResponse('NO')