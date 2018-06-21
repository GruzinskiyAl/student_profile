from apps.main.models import Student


def student_processor(request):
    if request.user.is_authenticated:
        return {'student' : Student.objects.get(user=request.user)}
    else:
        return {}