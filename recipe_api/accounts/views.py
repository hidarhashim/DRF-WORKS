from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import RecipeUserSerializer

# Create your views here.

class RecipeUserregister(APIView):
    def post(self,request):
        s=RecipeUserSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data,status=status.HTTP_201_CREATED)
        else:
            return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)