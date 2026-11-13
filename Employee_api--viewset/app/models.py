from django.db import models

class Employee(models.Model):

    gender_choices=(('male','Male'),('female','Female'))
    empid=models.IntegerField(unique=True)
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=10,choices=gender_choices)
    salary=models.IntegerField()
    designation=models.CharField(max_length=20)
    joining_year=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to='employees',null=True)

