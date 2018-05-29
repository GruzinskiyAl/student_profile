from django.db import models
from django.utils import timezone
from apps.main.models import Teacher, Student, UnivGroup
from django.utils.translation import ugettext_lazy as _

DAY_STATUS_CHOICES = (
    (1, _(u'Monday')),
    (2, _(u'Tuesday')),
    (3, _(u'Wednesday')),
    (4, _(u'Thursday')),
    (5, _(u'Friday')),
    (6, _(u'Saturday'))
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
        return str(self.subject)


class SubjectLecture(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    lecture_url = models.URLField(null=True, blank=True)
    description = models.TextField(_(u'Описание'), null=True, blank=True)

    def __str__(self):
        return str(self.subject)


class SubjectLab(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    lab_url = models.URLField(null=True, blank=True)
    description = models.TextField(_(u'Описание'), null=True, blank=True)

    def __str__(self):
        return str(self.subject)


class SubjectAdditionalMaterial(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    additional_material = models.TextField(null=True, blank=True)
    description = models.TextField(_(u'Описание'), null=True, blank=True)

    def __str__(self):
        return str(self.subject)


class SubjectOfUnivGroup(models.Model):
    group = models.ForeignKey(UnivGroup, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.IntegerField(choices=SEMESTER, default=1)
    closing_date = models.DateField(default=timezone.now)
    hours_count = models.IntegerField(default=100)

    class Meta:
        unique_together = ('group', 'subject')

    def __str__(self):
        return str(self.group) + '_' + str(self.subject)


class WeekSchedule(models.Model):
    day = models.IntegerField(choices=DAY_STATUS_CHOICES, default=1)
    lesson_num = models.IntegerField(choices=LESSON_STATUS_CHOICES, default=1)
    univ_group = models.ForeignKey(UnivGroup, on_delete=models.CASCADE)
    subject_numerator = models.ForeignKey(SubjectOfUnivGroup, related_name='числитель',
                                          on_delete=models.SET_NULL, null=True, blank=True, default=None)
    subject_denominator = models.ForeignKey(SubjectOfUnivGroup, related_name='знаменатель',
                                            on_delete=models.SET_NULL, null=True, blank=True, default=None)
    lecture_hall = models.CharField(_(u'Аудитория'), max_length=50, null=True)

    class Meta:
        unique_together=('day',
                         'lesson_num',
                         'univ_group')


class GroupExam(models.Model):
    subject = models.ForeignKey(SubjectOfUnivGroup, on_delete=models.CASCADE)
    univ_group = models.ForeignKey(UnivGroup, on_delete=models.CASCADE)
    exam_datetime = models.DateTimeField(default=timezone.now)
    lecture_hall = models.CharField(_(u'Аудитория'), max_length=50)

    class Meta:
        unique_together = ('subject', 'univ_group')

    def __str__(self):
        return str(self.subject) + '_' + str(self.exam_datetime)


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
        return self.student.FIO + '_' + self.subject.subject.name + '_' + str(self.full_mark)