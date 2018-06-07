from django.conf import settings
from django.conf.urls.static import static

from .views import (SubjectList, SubjectDebtList,
                    StudentSchedule, GroupExamList,
                    SubjectMaterial, UserPhotoSelect)
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', StudentSchedule.as_view(), name='schedule'),
    url(r'^subjects/$', SubjectList.as_view(), name='subject_list'),
    url(r'^subject/material/(?P<subject_pk>\d+)/$$',
        SubjectMaterial.as_view(), name='subject_material'),
    url(r'^debt/$', SubjectDebtList.as_view(), name='debt_list'),
    url(r'^exams/$', GroupExamList.as_view(), name='exam_list'),
    url(r'^photo/change/$', UserPhotoSelect.as_view(), name='change_photo')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
