from .views import (SubjectList, SubjectDebtList, StudentSchedule)
from django.conf.urls import url, include

urlpatterns = [
    url(r'^subjects/$', SubjectList.as_view(), name='subject_list'),
    url(r'^debt/$', SubjectDebtList.as_view(), name='debt_list'),
    url(r'^test/$', StudentSchedule.as_view(), name='schedule'),
]