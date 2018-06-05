# coding=utf-8

from django.db import models
from django.utils import timezone
from apps.main.models import Teacher, Student, UnivGroup
from django.utils.translation import ugettext_lazy as _

DAY_STATUS_CHOICES = (
    ('Monday', _(u'Понедельник')),
    ('Tuesday', _(u'Вторник')),
    ('Wednesday', _(u'Среда')),
    ('Thursday', _(u'Четверг')),
    ('Friday', _(u'Пятница')),
    ('Sunday', _(u'Суббота'))
)
LESSON_STATUS_CHOICES = [(i, i) for i in range(1, 9)]
EURO_MARK = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
    ('F', 'F'),
)
SIMPLE_MARK = [(i, i) for i in range(1, 6)]
SEMESTER = [(i, i) for i in range(1, 9)]


class Subject(models.Model):
    name = models.CharField(_(u'Название'), max_length=300, unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    description = models.TextField(_(u'Описание'), null=True, blank=True)

    def __str__(self):
        return str(self.name)


class SubjectLiterature(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    literature = models.TextField(null=True, blank=True)
    description = models.TextField(_(u'Описание'), null=True, blank=True)


    def __str__(self):
        return str(self.subject.name)


class SubjectLecture(models.Model):
    name = models.CharField(max_length=256, default='Лекция')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    lecture_url = models.URLField(null=True, blank=True)
    description = models.TextField(_(u'Описание'), null=True, blank=True)

    class Meta:
        ordering = ['pk', ]

    def __str__(self):
        return str(self.subject.name)


class SubjectLab(models.Model):
    name = models.CharField(max_length=256, default='Лабораторная работа')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    lab_url = models.URLField(null=True, blank=True)
    description = models.TextField(_(u'Описание'), null=True, blank=True)

    class Meta:
        ordering = ['pk', ]

    def __str__(self):
        return str(self.subject.name)


class SubjectAdditionalMaterial(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    additional_material = models.TextField(null=True, blank=True)
    description = models.TextField(_(u'Описание'), null=True, blank=True)

    def __str__(self):
        return str(self.subject.name)


class SubjectOfUnivGroup(models.Model):
    group = models.ForeignKey(UnivGroup, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.IntegerField(choices=SEMESTER, default=1)
    closing_date = models.DateField(default=timezone.now)
    hours_count = models.IntegerField(default=100)

    class Meta:
        unique_together = ('group', 'subject')
        ordering = ['semester', ]

    def __str__(self):
        return str(self.group.name) + '_' + str(self.subject.name)


class WeekSchedule(models.Model):
    day = models.CharField(choices=DAY_STATUS_CHOICES, default='Monday', max_length=20)
    lesson_num = models.IntegerField(choices=LESSON_STATUS_CHOICES, default=1)
    univ_group = models.ForeignKey(UnivGroup, on_delete=models.CASCADE)
    subject_numerator = models.ForeignKey(SubjectOfUnivGroup, related_name='числитель',
                                          on_delete=models.SET_NULL, null=True, blank=True, default=None)
    subject_denominator = models.ForeignKey(SubjectOfUnivGroup, related_name='знаменатель',
                                            on_delete=models.SET_NULL, null=True, blank=True, default=None)
    lecture_hall_numerator = models.CharField(_(u'Аудитория чис'), max_length=50, null=True, blank=True)
    lecture_hall_denominator = models.CharField(_(u'Аудитория знам'), max_length=50, null=True, blank=True)

    class Meta:
        unique_together = ('day',
                           'lesson_num',
                           'univ_group')
        ordering = ['day']

    def __str__(self):
        return str(self.univ_group.name) + '_' + str(self.day) + '_' + str(self.lesson_num)


class GroupExam(models.Model):
    subject = models.ForeignKey(SubjectOfUnivGroup, on_delete=models.CASCADE)
    univ_group = models.ForeignKey(UnivGroup, on_delete=models.CASCADE)
    exam_datetime = models.DateTimeField(default=timezone.now)
    lecture_hall = models.CharField(_(u'Аудитория'), max_length=50)

    class Meta:
        unique_together = ('subject', 'univ_group')

    def __str__(self):
        return str(self.subject.name) + '_' + str(self.exam_datetime)


class SubjectMark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(SubjectOfUnivGroup, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    full_mark = models.IntegerField(default=100)
    simple_mark = models.IntegerField(choices=SIMPLE_MARK, default=5)
    euro_mark = models.CharField(choices=EURO_MARK, default='A', max_length=1)
    na_status = models.BooleanField(default=True)

    class Meta:
        unique_together = ('student', 'subject')

    def __str__(self):
        return self.student.last_name + '_' + self.subject.subject.name + '_' + str(self.full_mark)
