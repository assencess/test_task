from django.db import models

class MyUser(models.Model):
    name = models.CharField(max_length=64, blank=False)
    
    def __str__(self):
        return self.name
        
class Device(models.Model):
    user = models.ForeignKey(MyUser, related_name="devices")
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    title = models.CharField(max_length=255, verbose_name='Faculty name')
    description = models.TextField(
        verbose_name='Faculty description', default='', blank=True)
#     #This is my field
#     objects = models.Manager()
#     students = FacultyStudentsManager()
    
    def __str__(self):
        return self.title

class Student(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='First name')
    last_name = models.CharField(max_length=255, verbose_name='Last name')
    birthday = models.DateField(verbose_name='User birthday')
    faculty = models.ForeignKey(Faculty, verbose_name='Faculty')
   
    def __str__(self):
        return self.first_name + " " + self.last_name