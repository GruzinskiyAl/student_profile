from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import *
from django.core.urlresolvers import reverse
import datetime
from apps.subject_controller.models import *


# Create your tests here.

class SubjectTestCase(TestCase):
    def setUp(self):
        user_student = User.objects.create_user(username='test_student',
                                                password='test_student')
        user_teacher = User.objects.create_user(username='test_teacher',
                                                password='test_teacher')
        group = UnivGroup.objects.create(group_name='KNgr-14-1',
                                         faculty='GRF',
                                         pulpit='GIS',
                                         curator=user_teacher)
        teacher = Teacher.objects.create(user=user_teacher,
                                         position='professor',
                                         t_number='0990000000',
                                         FIO='Korotenko G.M.')

        student = Student.objects.create(user=user_student,
                                         FIO='Gruzinskiy Alexandr',
                                         birth_date=datetime.date(1997, 8, 9),
                                         t_number='0660000000',
                                         univ_group=group)
        subject = Subject.objects.create(name='Test subject',
                                         teacher=teacher)
