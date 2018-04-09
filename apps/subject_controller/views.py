from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from .models import *
from apps.main.models import *
# Create your views here.

def SubjectList(request):
    try:
        student = Student.objects.get(user=request.user)
        group = student.univ_group
        subjects = SubjectOfUnivGroup.objects.filter(group=group)
        return render(request, 'index.html', {'subjects': subjects})
    except:
        return HttpResponse('NO')


