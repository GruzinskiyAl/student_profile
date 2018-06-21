from django.forms import ModelForm
from django import forms
from apps.main.models import Student


class ImageForm(ModelForm):
    # t_number = forms.CharField(max_length=10)
    # email = forms.EmailField
    # photo = forms.ImageField

    class Meta:
        model = Student
        fields = ['t_number', 'email', 'photo']
