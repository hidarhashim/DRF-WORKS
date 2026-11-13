from django.db.models import Model
from rest_framework import serializers
from app.models import Student

class Studentserializers(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    age = serializers.IntegerField()
    course =serializers.CharField(max_length=20)
    marks = serializers.IntegerField()

    def create(self,validated_data):
        s=Student.objects.create(**validated_data)
        s.save()
        return s
