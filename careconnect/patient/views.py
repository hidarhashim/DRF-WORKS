from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from patient.serializers import UserSerializer

from patient.serializers import PatientSerializer

from patient.models import Patient
from datetime import datetime,time,timedelta
#api view fro patient register

class Patientregister(APIView):
    def post(self,request):
        s=UserSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data,status=status.HTTP_201_CREATED)
        else:
            return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)

#api view for patient appointment booking
#patientappointmentlistcreateview

class PatientAppointmentListCreate(APIView):
    authentication_classes = [BasicAuthentication,] #to check whether user is authenticated or not
    permission_classes = [IsAuthenticated,] # only authenticated user can create booking
    def post(self,request):
        s=PatientSerializer(data=request.data)
        if s.is_valid():

            #token number , appointment time
            data=s.validated_data   #data after validation #all data is stored in dictionary
            d=data['doctor']
            date=data['appointment_date']   #fetches doctor and data from dictionary based on which token is given

            a=Patient.objects.filter(doctor=d,appointment_date=date).last()
            appointment_time=time(10,0,0) #10am
            if a:
                number=a.token_number+1
                appointment_time=(datetime.combine(date,a.appointment_time)+timedelta(minutes=15)).time()
            else:
                number=1

            s.save(token_number=number,appointment_time=appointment_time)
            return Response(s.data,status=status.HTTP_201_CREATED)

        else:
            return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)

