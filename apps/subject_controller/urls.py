from .views import SubjectList
from django.conf.urls import url, include

urlpatterns = [
    url(r'^subjects/$', SubjectList, name='subject_list'),
]