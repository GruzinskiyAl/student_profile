from django.db import models
from apps.main.models import Teacher, UnivGroup

DAY = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Sunday']
DAY_STATUS_CHOICES = sorted((day, day) for day in DAY)
LESSON_STATUS_CHOICES = [(i, i) for i in range(1, 9)]


class Subject(models.Model):
    name = models.CharField(max_length=300)
    teacer = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    descriprion = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class SubjectLiterature(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    literature = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.subject)


class SubjectLecture(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    lecture_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.subject)


class SubjectLab(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    lab_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.subject)


class SubjectAdditionalMaterial(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    additional_material = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.subject)


class SubjectOfUnivGroup(models.Model):
    group = models.ForeignKey(UnivGroup, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class DaySchedule(models.Model):
    lesson_num = models.CharField(choices=LESSON_STATUS_CHOICES, default=1)
    lecture_hall = models.CharField(max_length=50, null=True)
    subject_chisl = models.ForeignKey(SubjectOfUnivGroup, related_name='chisl_subject',
                                      on_delete=models.SET_NULL, null=True, blank=True, default=None)
    subject_znam = models.ForeignKey(SubjectOfUnivGroup, related_name='znam_subject',
                                     on_delete=models.SET_NULL, null=True, blank=True, default=None)


class WeekSchedule(models.Model):
    day = models.CharField(choices=DAY_STATUS_CHOICES, default='Monday')
    day_schedule = models.ForeignKey(DaySchedule, on_delete=models.SET_NULL, null=True)


class GroupExam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    univ_group = models.ForeignKey(UnivGroup, on_delete=models.CASCADE)
    exam_datetime = models.DateTimeField
    lecture_hall = models.CharField(max_length=50)