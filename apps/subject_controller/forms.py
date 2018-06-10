from django.forms import ModelForm
from apps.main.models import Student


class ImageForm(ModelForm):
    class Meta:
        model = Student
        fields = ['t_number', 'email', 'photo']