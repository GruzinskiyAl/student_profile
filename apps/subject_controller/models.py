# coding=utf-8
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from apps.main.models import Teacher, Student, UnivGroup
from django.utils.translation import ugettext_lazy as _
from .models_methods import mark_generation

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
SEMESTER = [(i, i) for i in [x * 0.5 for x in range(1, 17)]]


class Subject(models.Model):
    name = models.TextField(_(u'Название'), unique=True)
    teacher = models.ForeignKey(
        Teacher,
        verbose_name=u'Преподаватель')
    description = models.TextField(_(u'Описание'), null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Предмет'
        verbose_name = 'Предметы'


class SubjectLiterature(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        verbose_name=u'Предмет')
    literature = models.TextField(_(u'Литература'), null=True, blank=True)
    description = models.TextField(_(u'Описание'), null=True, blank=True)

    def __str__(self):
        return str(self.subject.name)

    class Meta:
        verbose_name_plural = 'Литература предмета'
        verbose_name = 'Литература предмета'


class SubjectLecture(models.Model):
    name = models.TextField(default='Лекция')
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        verbose_name=u'Предмет')
    lecture_url = models.URLField(null=True, blank=True)
    description = models.TextField(_(u'Описание'), null=True, blank=True)

    class Meta:
        ordering = ['pk', ]
        verbose_name_plural = 'Список лекций'
        verbose_name = 'Лекция'

    def __str__(self):
        return str(self.subject.name)


class SubjectLab(models.Model):
    name = models.TextField(default='Лабораторная работа')
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        verbose_name=u'Предмет')
    lab_url = models.URLField(null=True, blank=True)
    description = models.TextField(_(u'Описание'), null=True, blank=True)

    class Meta:
        ordering = ['pk', ]
        verbose_name_plural = 'Список лабораторных работ'
        verbose_name = 'Лабораторная работа'

    def __str__(self):
        return str(self.subject.name)


class SubjectAdditionalMaterial(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        verbose_name=u'Предмет')
    additional_material = models.TextField(
        null=True, blank=True, verbose_name=u'Материалы')
    description = models.TextField(_(u'Описание'), null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Дополнительные материалы'
        verbose_name = 'Дополнительные материалы'

    def __str__(self):
        return str(self.subject.name)


class SubjectOfUnivGroup(models.Model):
    group = models.ForeignKey(
        UnivGroup,
        on_delete=models.CASCADE,
        verbose_name=u'Группа',
        db_index=True)
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        verbose_name=u'Предмет', )
    start_semester = models.FloatField(
        choices=SEMESTER,
        default=1.0,
        verbose_name=u'Начальный семестр')
    semester_quantity = models.FloatField(
        choices=SEMESTER,
        default=1.0,
        verbose_name=u'Семестр окончания')
    hours_count = models.IntegerField(
        default=100, verbose_name=u'Количество часов')

    class Meta:
        unique_together = ('group', 'subject')
        ordering = ['start_semester', ]
        verbose_name_plural = 'Предметы группы'
        verbose_name = 'Предмет группы'

    def __str__(self):
        return str(self.subject.name) + '_' + str(self.group.group_name)


class WeekSchedule(models.Model):
    day = models.CharField(
        choices=DAY_STATUS_CHOICES,
        default='Monday',
        max_length=20,
        verbose_name=u'День недели')
    lesson_num = models.IntegerField(
        choices=LESSON_STATUS_CHOICES,
        default=1,
        verbose_name=u'Номер ленты')
    univ_group = models.ForeignKey(
        UnivGroup,
        on_delete=models.CASCADE,
        verbose_name=u'Группа',
        db_index=True)
    subject_numerator = models.ForeignKey(
        SubjectOfUnivGroup,
        related_name=u'числитель',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None)
    subject_denominator = models.ForeignKey(
        SubjectOfUnivGroup,
        related_name=u'знаменатель',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None)
    lecture_hall_numerator = models.CharField(
        _(u'Аудитория чис'), max_length=50, null=True, blank=True)
    lecture_hall_denominator = models.CharField(
        _(u'Аудитория знам'), max_length=50, null=True, blank=True)

    class Meta:
        unique_together = ('day',
                           'lesson_num',
                           'subject_numerator',
                           'subject_denominator')
        ordering = ['day']
        verbose_name_plural = 'Элементы расписания'
        verbose_name = 'Элемент расписания'

    def __str__(self):
        return str(self.univ_group.group_name) + '_' + \
               str(self.day) + '_' + str(self.lesson_num)


class GroupExam(models.Model):
    subject = models.ForeignKey(
        SubjectOfUnivGroup,
        on_delete=models.CASCADE,
        verbose_name=u'Предмет')
    univ_group = models.ForeignKey(
        UnivGroup,
        on_delete=models.CASCADE,
        verbose_name=u'Группа',
        db_index=True)
    exam_datetime = models.DateTimeField(
        default=timezone.now, verbose_name=u'Дата и время')
    lecture_hall = models.CharField(_(u'Аудитория'), max_length=50)

    class Meta:
        verbose_name_plural = 'Список экзаменов'
        verbose_name = 'Экзамен'
        unique_together = ('subject', 'univ_group')

    def __str__(self):
        return str(self.subject.subject.name) + '_' + str(self.exam_datetime)


class ExamSubjectMark(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name=u'Студент')
    subject = models.ForeignKey(
        SubjectOfUnivGroup,
        on_delete=models.CASCADE,
        verbose_name=u'Предмет')
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        verbose_name=u'Преподаватель')
    date = models.DateField(default=timezone.now, verbose_name=u'Дата')
    full_mark = models.IntegerField(default=1,
                                    validators=[
                                        MaxValueValidator(100),
                                        MinValueValidator(1)
                                    ], verbose_name=u'Оценка')
    simple_mark = models.IntegerField(
        choices=SIMPLE_MARK,
        default=5,
        verbose_name=u'Упрощенная оценка')
    euro_mark = models.CharField(
        choices=EURO_MARK,
        default='A',
        max_length=1,
        verbose_name=u'EU оценка')
    semester = models.FloatField(
        choices=SEMESTER,
        default=1.0,
        verbose_name=u'Семестр')

    class Meta:
        unique_together = ('student', 'subject', 'semester')
        verbose_name_plural = 'Оценоки по экзаменам'
        verbose_name = 'Оценка по экзамену'

    def __str__(self):
        return self.student.last_name + '_' + \
               self.subject.subject.name + '_' + str(self.full_mark)

    def __init__(self, *args, **kwargs):
        super(ExamSubjectMark, self).__init__(*args, **kwargs)
        self.set_mark()

    def set_mark(self):
        self.full_mark, self.simple_mark, self.euro_mark = mark_generation(self.full_mark)


class StudentSubjectMark(models.Model):
    subject = models.ForeignKey(
        SubjectOfUnivGroup,
        on_delete=models.CASCADE,
        verbose_name=u'Предмет')
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name=u'Студент')
    date = models.DateField(auto_now_add=True, verbose_name=u'Дата')
    semester = models.FloatField(
        choices=SEMESTER,
        default=1.0,
        verbose_name=u'Семестр')
    full_mark = models.IntegerField(default=100, validators=[
        MaxValueValidator(100),
        MinValueValidator(1)
    ], verbose_name=u'Оценка')
    simple_mark = models.IntegerField(
        choices=SIMPLE_MARK,
        default=5,
        verbose_name=u'Упрощенная оценка')
    euro_mark = models.CharField(
        choices=EURO_MARK,
        default='A',
        max_length=1,
        verbose_name=u'EU оценка')

    class Meta:
        verbose_name_plural = 'Оценки'
        verbose_name = 'Оценка'
        unique_together = ['student', 'subject', 'semester']
        ordering = ['semester']

    def __init__(self, *args, **kwargs):
        super(StudentSubjectMark, self).__init__(*args, **kwargs)
        self.set_mark()

    def set_mark(self):
        self.full_mark, self.simple_mark, self.euro_mark = mark_generation(self.full_mark)

    def __str__(self):
        return self.student.last_name + '_' + \
               self.subject.subject.name + '_' + str(self.full_mark)


class TeacherMessage(models.Model):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        verbose_name=u'Преподаватель')
    date = models.DateField(auto_now_add=True, verbose_name=u'Дата')
    univ_group = models.ForeignKey(
        UnivGroup,
        on_delete=models.CASCADE,
        verbose_name=u'Группа',
        db_index=True)
    message = models.TextField(verbose_name=u'Текст')

    def __str__(self):
        return str(self.date) + '_' + self.univ_group.group_name
