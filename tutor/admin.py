from django.contrib import admin
from .models import Course, Student, Teacher, Class, Applicant
# Register your models here.

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Applicant)
