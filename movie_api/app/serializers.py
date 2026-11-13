from rest_framework import serializers
from app.models import Movie
from django.contrib.auth.models import User
from django.core.mail import send_mail
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','id',
                'password',
                'email',
                'first_name',
                'last_name',]
        read_only_fields=['id']

    def create(self,validated_data):

        u=User.objects.create_user(**validated_data) #to encrypt the data or password hashing

        u.save()

        send_mail(subject='welcome to movie doctor',
                  message='Thank you for signing up for an account ',
                  from_email='hidarkhashim2@gmail.com',
                  recipient_list=[u.email],
                  fail_silently=True)
        return u