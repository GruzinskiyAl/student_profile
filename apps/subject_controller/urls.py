from django.conf import settings
from django.conf.urls.static import static

from .views import (SubjectList, SubjectDebtList,
                    StudentSchedule, GroupExamList,
                    SubjectMaterial, UserPhotoSelect,
                    StudentMarkBySubject)
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', StudentSchedule.as_view(), name='schedule'),
    url(r'^subjects/$', SubjectList.as_view(), name='subject_list'),
    url(r'^subjects/material/(?P<subject_pk>\d+)/$',
        SubjectMaterial.as_view(), name='subject_material'),
    url(r'^subjects/marks/(?P<subject_pk>\d+)/$',
        StudentMarkBySubject.as_view(), name='subject_marks'),
    url(r'^debt/$', SubjectDebtList.as_view(), name='debt_list'),
    url(r'^exams/$', GroupExamList.as_view(), name='exam_list'),
    url(r'^photo/change/$', UserPhotoSelect.as_view(), name='change_photo')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
