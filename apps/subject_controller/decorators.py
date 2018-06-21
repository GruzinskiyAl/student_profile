from django.http import HttpResponseRedirect
from apps.main.models import *


def auth_check(req):
    def wrapped_req(obj, request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                Student.objects.get(user=request.user)
                return req(obj, request, *args, **kwargs)
            except Student.DoesNotExist:
                try:
                    Teacher.objects.get(user=request.user)
                    return HttpResponseRedirect('/admin/')
                except Teacher.DoesNotExist:
                    return HttpResponseRedirect('/login/')
        else:
            return HttpResponseRedirect('/login/')
    return wrapped_req
