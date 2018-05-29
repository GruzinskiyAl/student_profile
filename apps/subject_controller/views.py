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
            group = student.univ_group
            subjects = SubjectOfUnivGroup.objects.filter(group=group)
            marks = SubjectMark.objects.filter(student=student)
            return render(request, 'index.html', {'subjects': subjects, 'student': student, 'marks': marks})
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


class StudentSchadule(View):

    def get(self, request):
        try:
            student = Student.objects.get(user=request.user)
            schadules = WeekSchedule.objects.filter(univ_group=student.univ_group)
            return render(request, 'schadule.html', {'schadules': schadules})
        except Student.DoesNotExist:
            return HttpResponse('NO')