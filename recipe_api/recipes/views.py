from django.db.models import Model, Q
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from recipes.serializers import RecipeSerializer
from recipes.models import Recipe

# Create your views here.
class RecipeCreateList(APIView):
    def post(self,request):
        s=RecipeSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data,status=status.HTTP_201_CREATED)
        else:
            return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        d=Recipe.objects.all()
        s=RecipeSerializer(d,many=True)
        return Response(s.data,status=status.HTTP_200_OK)

class RecipeRetreiveUpdateDelete(APIView):
    def get(self,request,pk):
        d=Recipe.objects.get(id=pk)
        s=RecipeSerializer(d)
        return Response(s.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        e=Recipe.objects.get(id=pk)
        s=RecipeSerializer(instance=e,data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        else:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        d=Recipe.objects.get(id=pk)
        d.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Search(APIView):
     def get(self,request):
         data=request.query_params.get('search')

         r=Recipe.objects.filter(Q(recipe_name__icontains=data)|Q(ingredients__icontains=data))

         s=RecipeSerializer(r,many=True)
         return Response(s.data,status=status.HTTP_200_OK)