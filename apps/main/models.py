from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=150)
    FIO = models.CharField(max_length=150)
    t_number = models.CharField(max_length=10)

    def __str__(self):
        return str(self.pk) + '_' + str(self.FIO)


class UnivGroup(models.Model):
    group_name = models.CharField(max_length=15, unique=True)
    faculty = models.CharField(max_length=150)
    pulpit = models.CharField(max_length=150)
    curator = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk) + '_' + str(self.group_name)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    FIO = models.CharField(max_length=150)
    birth_date = models.DateField
    t_number = models.CharField(max_length=10)
    univ_group = models.ForeignKey(UnivGroup, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.pk) + '_' + str(self.FIO)

