from django.contrib import admin
from .models import Student, UnivGroup, Teacher

# Register your models here.

admin.site.register(Student, admin.ModelAdmin)
admin.site.register(UnivGroup, admin.ModelAdmin)
admin.site.register(Teacher, admin.ModelAdmin)