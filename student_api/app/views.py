
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads
from django.http import JsonResponse
from django.views import View
from rest_framework.response import Response
from app.models import Student
from rest_framework.views import APIView
from app.serializers import Studentserializers




class studentlist(APIView):
    def get(self, request):

        qs=Student.objects.all()  #code to covert to list of dictionaries

        serializers_instance=Studentserializers(qs,many=True)

        return Response(serializers_instance.data)


class Studentcreate(APIView):
    def post(self,request):
        d=request.data
        serializers_instance=Studentserializers(data=d)
        if serializers_instance.is_valid():
            serializers_instance.save()
            return Response({'message':'created'})
        else:
            return Response(serializers_instance.errors)


    #to retrieve a specific record, so an extra id argument is needed to retreive
class StudentDetail(View):
    def get(self,request,i): #i stores the id value coming from client

            #read record matching with id from db table
        qs=Student.objects.filter(id=i)

            #convert the data(model object) into python native list
        data=list(qs.values())

            #send the response
        return JsonResponse(data,safe=False)


#api view fro deleting a specific record
@method_decorator(csrf_exempt,name='dispatch')
class StudentDelete(View):
    def delete(self,request,i):
        #read record matching with id from the db table
        s=Student.objects.get(id=i)

        #delete the record
        s.delete()

        #send response
        return JsonResponse({'message':'deleted successfully'})


#api view for updating(fully) existing record
@method_decorator(csrf_exempt,name='dispatch')
class StudentUpdate(View):
    def put(self,request,i):

        #read the record matching with id from db table
        s=Student.objects.get(id=i)

        #fetch data from client side
        form_data=request.body #json

        #convert json to python native
        data=loads(form_data)

        # update each feild in db table
        s.name=data['name']
        s.age=data['age']
        s.course=data['course']
        s.marks=data['marks']


        #save the record
        s.save()

        #return response
        return JsonResponse({'message':'updated successfully'})


#api view for partially updating existing record
@method_decorator(csrf_exempt,name='dispatch')
class StudentPartialUpdation(View):
    def patch(self,request,i):
        s=Student.objects.get(id=i)

        form_data=request.body

        data=loads(form_data)
        print(data)

        if 'name' in data:
            s.name=data['name']

        if 'age' in data:
            s.age=data['age']

        if 'course' in data:
            s.course=data['course']

        if 'marks' in data:
            s.marks=data['marks']

        s.save()

        return JsonResponse({'message':'partial updation successful'})