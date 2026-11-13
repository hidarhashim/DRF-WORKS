from django.contrib.sessions import serializers
from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import Movie
from app.serializers import MovieSerializer

class Moviecreate(APIView):
    def post(self,request):
        d=request.data
        serializer_instance=MovieSerializer(data=d)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message":"created successfully"})
        else:
            return Response(serializer_instance.errors)

class Movielist(APIView):
    def get(self,request):
        qs=Movie.objects.all()
        serializer_instance=MovieSerializer(qs,many=True)
        return Response(serializer_instance.data)

class Movieretrieve(APIView):
    def get(self,request,i):
        e=get_object_or_404(Movie,id=i)
        si=MovieSerializer(e)
        return Response(si.data)

class Movieupdate(APIView):
    def put(self,request,i):
        d=request.data
        e=get_object_or_404(Movie,id=i)
        si=MovieSerializer(instance=e,data=d)
        if si.is_valid():
            si.save()
            return Response({'message':'successfully'})
        else:
            return Response(si.errors)


class Moviepartialupdate(APIView):
    def patch(self,request,i):
        d=request.data
        e=get_object_or_404(Movie,id=i)
        si=MovieSerializer(instance=e,data=d,partial=True)
        if si.is_valid():
            si.save()
            return Response({'message':'successfully'})
        else:
            return Response(si.errors)

class Moviedelete(APIView):
    def delete(self,request,i):
        e=get_object_or_404(Movie,id=i)
        e.delete()
        return Response({'message':'deleted successfully'})