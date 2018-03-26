from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Subject, admin.ModelAdmin)
admin.site.register(Schedule, admin.ModelAdmin)
admin.site.register(SubjectLiterature, admin.ModelAdmin)
admin.site.register(SubjectLecture, admin.ModelAdmin)
admin.site.register(SubjectLab, admin.ModelAdmin)
admin.site.register(SubjectAdditionalMaterial, admin.ModelAdmin)
admin.site.register(SubjectOfUnivGroup, admin.ModelAdmin)
