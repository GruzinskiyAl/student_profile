from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib import auth
from apps.subject_controller.models import (SubjectOfUnivGroup, SubjectMark,
                                            WeekSchedule, GroupExam, Subject)
from apps.main.models import *
from .to_dict_functions import schedule_for_template, subject_materials_for_template


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
            schedules_queryset = WeekSchedule.objects.filter(univ_group=student.univ_group)
            return render(request, 'schedule.html', {'day_list': schedule_for_template(schedules_queryset),
                                                     'student': student})
        except (Student.DoesNotExist,):
            return HttpResponse('NO')


class GroupExamList(View):

    def get(self, request):
        try:
            student = Student.objects.get(user=request.user)
            exam_list = GroupExam.objects.filter(univ_group=student.univ_group,
                                                 exam_datetime__gt=datetime.now())
            return render(request, 'exam_list.html', {'student': student, 'exam_list': exam_list})
        except (Student.DoesNotExist,):
            return HttpResponse('NO')


class SubjectMaterial(View):

    def get(self, request, subject_pk):
        try:
            student = Student.objects.get(user=request.user)
            subject = Subject.objects.get(pk=subject_pk)
            labs, lectures, literature_list, materials = subject_materials_for_template(subject)
            return render(request, 'subject_material.html', {'labs': labs,
                                                             'lectures': lectures,
                                                             'literature_list': literature_list,
                                                             'materials': materials,
                                                             'student': student,
                                                             'subject': subject})
        except (Student.DoesNotExist,):
            return HttpResponse('NO')


class LoginUser(View):

    def post(self, request, login, password):
        return