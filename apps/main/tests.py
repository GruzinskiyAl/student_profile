from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import *
from django.core.urlresolvers import reverse
import datetime
from apps.subject_controller.models import *


# Create your tests here.

class SubjectTestCase(TestCase):
    def setUp(self):
        user_student_1 = User.objects.create_user(username='test_student_1',
                                                  password='test_student_1')
        user_teacher_1 = User.objects.create_user(username='test_teacher_1',
                                                  password='test_teacher_1')
        user_student_2 = User.objects.create_user(username='test_student_2',
                                                  password='test_student_2')
        user_teacher_2 = User.objects.create_user(username='test_teacher_2',
                                                  password='test_teacher_2')

        teacher_1 = Teacher.objects.create(user=user_teacher_1,
                                           position='professor',
                                           t_number='0990000000',
                                           FIO='Korotenko G.M.')

        teacher_2 = Teacher.objects.create(user=user_teacher_2,
                                           position='professor',
                                           t_number='0990000231',
                                           FIO='Garkusha I.N.')

        group_1 = UnivGroup.objects.create(group_name='KNgr-14-1',
                                           faculty='GRF',
                                           pulpit='GIS',
                                           curator=teacher_1)
        student_1 = Student.objects.create(user=user_student_1,
                                           FIO='Gruzinskiy A.P.',
                                           birth_date=datetime.date(1997, 8, 9),
                                           t_number='0660000000',
                                           univ_group=group_1)

        student_2 = Student.objects.create(user=user_student_2,
                                           FIO='Kurochkin E.G.',
                                           birth_date=datetime.date(1997, 1, 1),
                                           t_number='0660000000',
                                           univ_group=group_1)

        subject_1 = Subject.objects.create(name='Test subject_1',
                                           teacher=teacher_1)
        SubjectLiterature.objects.create(subject=subject_1,
                                         literature='https://literature.com')
        SubjectLecture.objects.create(subject=subject_1,
                                      lecture_url='https://lecture.com')
        SubjectLab.objects.create(subject=subject_1,
                                  lab_url='https://lab.com')
        SubjectAdditionalMaterial.objects.create(subject=subject_1,
                                                 additional_material='https://materials.com')
        subject_2 = Subject.objects.create(name='Test subject_2',
                                           teacher=teacher_2)

        subject_of_group_1 = SubjectOfUnivGroup.objects.create(subject=subject_1,
                                                               group=group_1,
                                                               semester=8,
                                                               closing_date = datetime.date(2018, 5, 30))

        subject_of_group_2 = SubjectOfUnivGroup.objects.create(subject=subject_2,
                                                               group=group_1,
                                                               semester=8,
                                                               closing_date=datetime.date(2018, 5, 30))
        WeekSchedule.objects.create(day=1,
                                    lesson_num=1,
                                    univ_group=group_1,
                                    subject_numerator=subject_of_group_1,
                                    lecture_hall='1/78')
        WeekSchedule.objects.create(day=3,
                                    lesson_num=3,
                                    univ_group=group_1,
                                    subject_denominator=subject_of_group_2,
                                    lecture_hall='1/78')
        GroupExam.objects.create(subject=subject_of_group_1,
                                 univ_group=group_1,
                                 exam_datetime=datetime.datetime(year=2018,
                                                                 month=1,
                                                                 day=1,
                                                                 hour=1,
                                                                 minute=1),
                                 lecture_hall='1/78')
        SubjectMark.objects.create(student=student_1,
                                   subject=subject_of_group_1,
                                   teacher=teacher_1,
                                   date=datetime.datetime(year=2018,
                                                          month=5,
                                                          day=1),
                                   full_mark=95,
                                   simple_mark=5,
                                   euro_mark='A',
                                   na_status=False)

    def test_main_model(self):
        student = Student.objects.get(user=User.objects.get(username='test_student_1'))
        teacher = Teacher.objects.get(user=User.objects.get(username='test_teacher_1'))
        group = UnivGroup.objects.get(curator=teacher)

        self.assertEqual(Student.objects.all().count(), 2)
        self.assertEqual(UnivGroup.objects.all().count(), 1)
        self.assertEqual(Teacher.objects.all().count(), 2)
        self.assertEqual(User.objects.all().count(), 4)
        self.assertEqual(student.FIO, 'Gruzinskiy A.P.')
        self.assertEqual(teacher.FIO, 'Korotenko G.M.')
        self.assertEqual(group.group_name, 'KNgr-14-1')
        self.assertEqual(student.univ_group.curator.position, 'professor')
        self.assertEqual(student.univ_group.faculty, 'GRF')

    def test_subj_model(self):
        teacher = Teacher.objects.get(user=User.objects.get(username='test_teacher_1'))
        univ_group = UnivGroup.objects.get(curator=teacher)
        subject = Subject.objects.get(teacher=teacher)
        subject_group = SubjectOfUnivGroup.objects.get(group=univ_group, subject=subject)
        exam = GroupExam.objects.get(subject=subject_group, univ_group=univ_group)

        self.assertEqual(Subject.objects.all().count(), 2)
        self.assertEqual(SubjectLecture.objects.all().count(), 1)
        self.assertEqual(SubjectLiterature.objects.all().count(), 1)
        self.assertEqual(SubjectLab.objects.all().count(), 1)
        self.assertEqual(SubjectAdditionalMaterial.objects.all().count(), 1)
        self.assertEqual(SubjectOfUnivGroup.objects.all().count(), 2)
        self.assertEqual(WeekSchedule.objects.all().count(), 2)
        self.assertEqual(GroupExam.objects.all().count(), 1)
        self.assertEqual(SubjectMark.objects.all().count(), 1)
        self.assertEqual(exam.subject.subject.teacher, teacher)
        self.assertEqual(exam.subject.group.group_name, 'KNgr-14-1')
        self.assertEqual(exam.subject.group.curator, teacher)
        self.assertEqual(SubjectOfUnivGroup.objects.filter(group=univ_group).count(), 2)
