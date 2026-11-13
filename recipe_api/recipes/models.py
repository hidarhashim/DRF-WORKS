from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name=models.CharField(max_length=30)
    ingredients=models.CharField(max_length=30)
    instructions=models.CharField(max_length=100)
    mealtype=models.TextField()
    cuisine=models.CharField(max_length=30)
    image=models.ImageField(upload_to='recipes',null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True,null=True)