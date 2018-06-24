# coding=utf-8
import random
from math import trunc
from operator import itemgetter
from .models import *
from django.db.models import Max, Avg
from .models_methods import mark_generation

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
                schedule_obj = schedule_queryset.get(
                    day=en_day, lesson_num=lesson)
                if schedule_obj.subject_numerator:
                    subject_num = 'Чс: ' + schedule_obj.subject_numerator.subject.name
                    subject_num += ' ' + \
                                   str(schedule_obj.subject_numerator.subject.teacher.name_initials_string())
                    subject_num += ' ' + \
                                   str(schedule_obj.lecture_hall_numerator)
                if schedule_obj.subject_denominator:
                    subject_denom = subject_denom + ' Зн: ' + \
                                    schedule_obj.subject_denominator.subject.name
                    subject_denom += ' ' + \
                                     str(schedule_obj.subject_denominator.subject.teacher.name_initials_string())
                    subject_denom += ' ' + \
                                     str(schedule_obj.lecture_hall_denominator)
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
    material = SubjectAdditionalMaterial.objects.filter(
        subject=group_subject_object)
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


def chart_marks_data(student):
    data = []
    student_marks = StudentSubjectMark.objects.filter(student=student)
    for i, i in SEMESTER:
        semester_marks = student_marks.filter(semester=i)
        value = 0
        for mark in semester_marks.values_list('full_mark'):
            value += int(mark[0])
        if semester_marks.count() != 0:
            avg_mark = round(value / semester_marks.count(), 2)
            data.append([str(i) + u' семестр', avg_mark])
    return data


def group_rating(student, semester):
    group = student.univ_group
    students = Student.objects.filter(univ_group=group)
    stipend_percent = round(students.count() * 0.4)
    data = []
    for stud in students:
        stud_mark = {}
        avg_mark = ExamSubjectMark.objects.filter(student=stud,
                                                  semester=semester).aggregate(Avg('full_mark'))['full_mark__avg']
        if avg_mark:
            stud_mark['student'] = stud
            stud_mark['avg_mark'] = mark_generation(round(avg_mark))
            data.append(stud_mark)
    data = sorted(data, key=itemgetter('avg_mark'), reverse=True)
    stipend = data[:stipend_percent]
    non_stipend = data[stipend_percent:]
    return stipend, non_stipend, semester


def group_chart_marks_data(request_student):
    group = request_student.univ_group
    students_count = Student.objects.filter(univ_group=group).count()
    data = []
    for i, i in SEMESTER:
        sum_avg_mark = 0
        for student in Student.objects.filter(univ_group=group):
            marks = StudentSubjectMark.objects.filter(student=student, semester=i)
            stud_avg_mark = marks.aggregate(Avg('full_mark'))['full_mark__avg']
            if stud_avg_mark:
                sum_avg_mark += stud_avg_mark
        if students_count != 0 and StudentSubjectMark.objects.filter(semester=i).count() != 0:
            avg_mark = round(sum_avg_mark / students_count, 2)
            data.append([str(i) + u' семестр', avg_mark])
    return data
