from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(_(u'Ученая степень'), max_length=150)
    FIO = models.CharField(_(u'ФИО'),max_length=150)
    t_number = models.CharField(_(u'Номер телефона'), max_length=10)
    email = models.EmailField(_(u'Почта'), null=True, blank=True)

    def __str__(self):
        return str(self.pk) + '_' + str(self.FIO)


class UnivGroup(models.Model):
    group_name = models.CharField(_(u'Название'), max_length=15, unique=True)
    faculty = models.CharField(_(u'Факультет'), max_length=150)
    pulpit = models.CharField(_(u'Кафедра'), max_length=150)
    curator = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    enter_date = models.DateField(default=timezone.now)
    finish_date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['group_name']

    def __str__(self):
        return str(self.group_name)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    FIO = models.CharField(_(u'ФИО'),max_length=150)
    birth_date = models.DateField(null=True)
    t_number = models.CharField(_(u'Номер телефона'), max_length=10)
    email = models.EmailField(_(u'Почта'), null=True, blank=True)
    univ_group = models.ForeignKey(UnivGroup, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['univ_group']

    def __str__(self):
        return str(self.pk) + '_' + str(self.FIO)

