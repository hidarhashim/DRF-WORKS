from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    description=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    completed=models.BooleanField(default=False)