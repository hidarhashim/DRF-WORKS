from tkinter.constants import CASCADE

from django.db import models

from doctor.models import Doctor


# Create your models here.
class Patient(models.Model):
    choice=(('male','Male'),('female','Female'))
    patient_name=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=20,choices=choice)
    phone=models.CharField(max_length=20)
    appointment_time=models.TimeField(null=True,blank=True)
    appointment_date=models.DateField()
    token_number=models.IntegerField(null=True)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True,null=True)