from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from apps.subject_controller.models import (SubjectOfUnivGroup, ExamSubjectMark,
                                            WeekSchedule, GroupExam, Subject,
                                            StudentSubjectMark, TeacherMessage)
from apps.main.models import *
from .to_dict_functions import (schedule_for_template,
                                subject_materials_for_template,
                                subject_list_with_marks,
                                chart_marks_data)
from .forms import ImageForm


class SubjectList(View):
    def get(self, request):
        if request.user.is_authenticated:
            try:
                student = Student.objects.get(user=request.user)
                subjects_dict = subject_list_with_marks(student)
                return render(request, 'subject_list.html', {'subjects_with_mark': subjects_dict, 'student': student})
            except Student.DoesNotExist:
                return redirect('/login/')
        else:
            return redirect('/login/')


class StudentSchedule(View):

    def get(self, request):
        if request.user.is_authenticated:
            try:
                student = Student.objects.get(user=request.user)
                schedules_queryset = WeekSchedule.objects.filter(univ_group=student.univ_group)
                return render(request, 'schedule.html', {'day_list': schedule_for_template(schedules_queryset),
                                                         'student': student})
            except Student.DoesNotExist:
                return redirect('/login/')
        else:
            return redirect('/login/')


class GroupExamList(View):

    def get(self, request):
        if request.user.is_authenticated:
            try:
                student = Student.objects.get(user=request.user)
                exam_list = GroupExam.objects.filter(univ_group=student.univ_group,
                                                     exam_datetime__gt=datetime.now())
                return render(request, 'exam_list.html', {'student': student, 'exam_list': exam_list})
            except Student.DoesNotExist:
                return redirect('/login/')
        else:
            return redirect('/login/')


class SubjectMaterial(View):

    def get(self, request, subject_pk):
        if request.user.is_authenticated:
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
            except Student.DoesNotExist:
                return redirect('/login/')
        else:
            return redirect('/login/')


# class UserPhotoSelect(View):

def update_image(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
            user = request.user
            student = Student.objects.get(user=user)
            if form.is_valid():
                student.photo = request.FILES['photo']
                student.t_number = request.POST['t_number']
                student.email = request.POST['email']
                student.save()
                return HttpResponseRedirect(reverse('schedule'))
        else:
            form = ImageForm()
        return render(request, 'image_search.html', {'form':form})
    else:
        return redirect('/login/')


class StudentMarkBySubject(View):

    def get(self, request, subject_pk):
        if request.user.is_authenticated:
            try:
                student = Student.objects.get(user=request.user)
                subject = SubjectOfUnivGroup.objects.get(pk=subject_pk)
                marks = StudentSubjectMark.objects.filter(student=student, subject=subject)
                return render(request, 'subject_marks.html', {'student': student,
                                                              'marks': marks,
                                                              'subject': subject})
            except Student.DoesNotExist:
                return redirect('/login/')
        else:
            return redirect('/login/')


class StudentMarksChart(View):

    def get(self, request):
        if request.user.is_authenticated:
            try:
                student = Student.objects.get(user=request.user)
                return render(request, 'marks_chart.html', {'student': student,
                                                            'values': chart_marks_data(student)})
            except Student.DoesNotExist:
                return redirect('/login/')
        else:
            return redirect('/login/')


class TeacherMessages(View):

    def get(self, request):
        if request.user.is_authenticated:
            try:
                student = Student.objects.get(user=request.user)
                messages = TeacherMessage.objects.filter(univ_group=student.univ_group)
                return render(request, 'teachers_messages.html', {'student': student,
                                                                 'messages': messages})
            except Student.DoesNotExist:
                return redirect('/login/')
        else:
            return redirect('/login/')
