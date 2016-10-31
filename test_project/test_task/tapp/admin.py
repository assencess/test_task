from django.contrib import admin
from .models import Device, Faculty, MyUser, Student

admin.site.register(Device)
admin.site.register(Faculty)
admin.site.register(MyUser)
admin.site.register(Student)