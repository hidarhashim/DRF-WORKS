from urllib import request

from django.contrib.sessions import serializers
from django.shortcuts import render, get_object_or_404
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import Movie
from app.serializers import MovieSerializer

#########################################################################
# apiview

# class MovieListCreate(APIView):
#     def get(self,request):
#         qs=Movie.objects.all()
#         s=MovieSerializer(qs,many=True)
#         return Response(s.data,status=status.HTTP_200_OK)
#
#     def post(self,request):
#         d=request.data
#         s = MovieSerializer(data=d)
#         if s.is_valid():
#             s.save()
#             return Response(s.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
# class MovieRetrieveUpdateDelete(APIView):
#     def get(self,request,i):
#         qs=get_object_or_404(Movie,id=i)
#         s=MovieSerializer(qs)
#         return Response(s.data,status=status.HTTP_200_OK)
#
#     def put(self,request,i):
#         d=request.data
#         e=get_object_or_404(Movie,id=i)
#         s=MovieSerializer(data=d,instance=e)
#         if s.is_valid():
#             s.save()
#             return Response(s.data,status=status.HTTP_200_OK)
#         else:
#             return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self,request,i):
#         d = request.data
#         e = get_object_or_404(Movie, id=i)
#         s = MovieSerializer( data=d,instance=e,partial=True)
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=status.HTTP_200_OK)
#         else:
#             return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, i):
#         e=get_object_or_404(Movie,id=i)
#         e.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#########################################################################################
# # # mixin
#
# from rest_framework import mixins,generics
# class MovieListCreate(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
#
# class MovieRetrieveUpdateDelete(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin ,generics.GenericAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#
#     def put(self,request,pk):
#         return  self.update(request,pk)
#
#     def delete(self,request,pk):
#         return self.destroy(request,pk)

#################################################################################
## generic
# from rest_framework import generics
# class MovieListCreate(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
# class MovieRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

##################################################################
## veiwset

from rest_framework import viewsets

class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer