from django.contrib.auth.models import User

from rest_framework import serializers


class RecipeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']

    def create(self,validated_data):
        u=User.objects.create_user(**validated_data)
        u.save()
        return u