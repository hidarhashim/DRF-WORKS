from functools import partial

from django.db.migrations import serializer
from django.db.models import Model
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from app.models import Employee
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads
from rest_framework.response import Response

from rest_framework.views import APIView     #Django restframework
from app.serializers import EmployeeSerializer
from rest_framework import status
###################################################################################
from rest_framework import viewsets
class EmployeeView(viewsets.ModelViewSet):   #GET+POST+PUT+GET(ID)+ PATCH+DELETE
    #combined  view of primary key and non primary key operations
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


################################################################################
# All codes below is replaced by the code above
##############################################################################

# #rest_framework
# class Employeecreate(APIView):
#     def post(self,request):
#         # form_data=request.body     #queryset
#         # data=loads(form_data)      #
#
#         #calls EmployeeSerialization for deserialization
#         d=request.data        #python native type
#         serializer_instance=EmployeeSerializer(data=d)     #desserialization
#
#         #chech whether the d is valid if valid the validated data is saved to table
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response({'message':'created'},status=status.HTTP_201_CREATED)
#
#         #if not valid it will raise error
#         else:
#             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
# class Employeelist(APIView):
#     def get(self,request):
#         #read all data from db table
#         qs=Employee.objects.all()
#
#         #calls EmployeeSerializer class fro coonverting qs into python native type
#         serializer_instance=EmployeeSerializer(qs,many=True) ##many=True (multiple employee record for conversion)
#
#         #sent the serialized data into client side as json using Response()
#         return Response(serializer_instance.data,status=status.HTTP_200_OK)
#
# #get by id or retrieve
# class EmployeeRetrieve(APIView):
#     def get(self,request,i):
#         #e=Employee.objects.get(id=i)
#         e=get_object_or_404(Employee,id=i)# handles exemption automatically and sends the response 404 Not Fpund if no matching record is found
#         serializer_instance=EmployeeSerializer(e)
#         return Response(serializer_instance.data,status=status.HTTP_200_OK)
#
#
# class Employeeupdate(APIView):
#     def put(self,request,i):
#         # fetches data coming from client side
#         d=request.data
#
#         #read the record from db table matching the id
#         e=get_object_or_404(Employee,id=i)
#
#         #calls the serializer class for deserialization(conversion+validation)
#         serializer_instance=EmployeeSerializer(instance=e,data=d)
#
#         # after validation saves the record
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
# class Employeepartialupdate(APIView):
#     def patch(self, request, i):
#         # fetches data coming from client side
#         d = request.data
#
#         # read the record from db table matching the id
#         e = get_object_or_404(Employee, id=i)
#
#         # calls the serializer class for deserialization(conversion+validation)
#         serializer_instance = EmployeeSerializer(instance=e, data=d,partial=True)
#
#         # after validation saves the record
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
#
# class Employeedelete(APIView):
#     def delete(self,request,i):
#         e=get_object_or_404(Employee,id=i)
#         e.delete()
#         return Response({"message":"deleted successfully"},status=status.HTTP_204_NO_CONTENT)