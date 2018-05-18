from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib import auth
from apps.subject_controller.models import SubjectOfUnivGroup, SubjectMark
from apps.main.models import *


class SubjectList(View):
    def get(self, request):
        try:
            student = Student.objects.get(user=request.user)
            group = student.univ_group
            subjects = SubjectOfUnivGroup.objects.filter(group=group)
            return render(request, 'index.html', {'subjects': subjects})
        except Student.DoesNotExist:
            return HttpResponse('NO')

class SubjectDebtList(View):
    def get(self, request):
        student = Student.objects.get(user=request.user)
        group = student.univ_group
        subjects = SubjectOfUnivGroup.objects.filter(group=group)
        marks = SubjectMark.objects.exclude(subjects__in=subjects)
