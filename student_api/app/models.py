from django.db import models
from django.db.models.fields import CharField


# Create your models here.


#definition of table schema/structure
class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    course=models.CharField(max_length=20)
    marks=models.IntegerField()



class Course(models.Model):
    mode_choices=(('offline',"OFFLINE"),('online',"ONLINE"))
    course_name=models.CharField(max_length=20)
    instructor=models.CharField(max_length=20)
    fee=models.IntegerField()
    duration=models.CharField(max_length=20)
    mode=models.CharField(max_length=20,choices=mode_choices)