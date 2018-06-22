from PIL import Image
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(_(u'Ученая степень'), max_length=150)
    first_name = models.CharField(_(u'Имя'), max_length=150)
    last_name = models.CharField(_(u'Фамилия'), max_length=150)
    patronymic = models.CharField(_(u'Отчество'), max_length=150)
    t_number = models.CharField(_(u'Номер телефона'), max_length=10)
    email = models.EmailField(_(u'Почта'), null=True, blank=True)
    photo = models.ImageField(upload_to='user_media', null=True, blank=True)
    about = models.TextField(_(u'О себе'), blank=True, null=True)

    def __str__(self):
        return str(self.last_name) + '_' + \
            str(self.first_name) + '_' + str(self.pk)

    def name_initials_string(self):
        return self.last_name + ' ' + \
            self.first_name[0] + '.' + ' ' + self.patronymic[0] + '.'


class UnivGroup(models.Model):
    group_name = models.CharField(_(u'Название'), max_length=15, unique=True)
    faculty = models.CharField(_(u'Факультет'), max_length=150)
    pulpit = models.CharField(_(u'Кафедра'), max_length=150)
    curator = models.ForeignKey(Teacher)
    enter_date = models.DateField(default=timezone.now)
    finish_date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['group_name']

    def __str__(self):
        return str(self.group_name)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stud_number = models.CharField(max_length=10)
    first_name = models.CharField(_(u'Имя'), max_length=150)
    last_name = models.CharField(_(u'Фамилия'), max_length=150)
    patronymic = models.CharField(_(u'Отчество'), max_length=150)
    t_number = models.CharField(_(u'Номер телефона'), max_length=10)
    email = models.EmailField(_(u'Почта'), null=True, blank=True)
    univ_group = models.ForeignKey(
        UnivGroup, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(
        _(u'Фото'),
        upload_to='user_media',
        null=True,
        blank=True)

    class Meta:
        ordering = ['univ_group']

    def __str__(self):
        return str(self.last_name) + '_' + \
            str(self.first_name) + '_' + str(self.pk)
