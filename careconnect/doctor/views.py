from django.db.models import Model
from django.shortcuts import render, get_object_or_404
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from doctor.serializers import DoctorSerializer
from rest_framework import status
from doctor.models import Doctor
#creating a new doctor record


#listing all doctor

#reading all doctors


#updating details of a doctor

#deleting a doctor record

#filtering doctor  details based on specification

from doctor.permissions import IsAdminUserOrReadOnly
class DoctorListCreate(APIView):
    permission_classes = [IsAdminUserOrReadOnly]   #only admin can perfrom list/create
    authentication_classes = [BasicAuthentication,]  #username/password
    def get(self,request):
        d=Doctor.objects.all()
        s=DoctorSerializer(d,many=True)
        return Response(s.data,status=status.HTTP_200_OK)

    def post(self,request):
        s=DoctorSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data,status=status.HTTP_201_CREATED)
        else:
            return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)


class DoctorRetrieveUpdateDelete(APIView):
    permission_classes = [IsAdminUserOrReadOnly]  # only admin can perform update
    authentication_classes = [BasicAuthentication, ]
    def get(self,request,pk):
        d=get_object_or_404(Doctor,id=pk)
        s=DoctorSerializer(d)
        return Response(s.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        d=get_object_or_404(Doctor,id=pk)
        s=DoctorSerializer(instance=d,data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data,status=status.HTTP_201_CREATED)
        else:
            return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        d=get_object_or_404(Doctor,id=pk)
        d.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# to filter doctor details based on specification
class DoctorSearch(APIView):
    def get(self,request):
        data=request.query_params.get('search')

        d=Doctor.objects.filter(specialization=data)
        s=DoctorSerializer(d,many=True)
        return Response(s.data,status=status.HTTP_200_OK)


#api view for creating admin user
from doctor.serializers import UserSerializer

class AdminRegister(APIView):
    def post(self,request):
        s=UserSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data,status=status.HTTP_201_CREATED)
        else:
            return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)