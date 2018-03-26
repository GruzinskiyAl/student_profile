from django.db import models
from apps.main.models import Teacher, Student, UnivGroup

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Sunday']
WEEK_DAYS = sorted((day, day) for day in DAYS)

class Subject(models.Model):
    name = models.CharField(max_length=300)
    teacer = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    descriprion = models.TextField


class SubjectLiterature(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    literature = models.TextField


class SubjectLecture(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    lecture_url = models.URLField


class SubjectLab(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    lab_url = models.URLField


class SubjectAdditionalMaterial(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    additional_material = models.TextField


class SubjectOfUnivGroup(models.Model):
    group = models.ForeignKey(UnivGroup, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class Schedule(models.Model):
    day = models.CharField(choices=WEEK_DAYS, default='Monday', max_length=15)
    lesson_num = models.IntegerField
    lecture_hall = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    univ_group = models.ForeignKey(UnivGroup, on_delete=models.CASCADE)
