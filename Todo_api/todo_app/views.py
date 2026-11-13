from functools import partial

from django.db.models import Model
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from todo_app.models import Todo
from todo_app.serializers import TodoSerializer

from todo_app.permissions import IsOwner


class TodoListCreate(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        d=Todo.objects.filter(user=request.user)
        s=TodoSerializer(d,many=True)
        return Response(s.data,status=status.HTTP_200_OK)


    def post(self,request):
        u=request.user
        s=TodoSerializer(data=request.data)
        if s.is_valid():
            s.save(user=u)
            return Response(s.data,status=status.HTTP_201_CREATED)
        else:
            return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)

class TodoDetail(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated,IsOwner ]

    def get(self,request,pk):

        d=Todo.objects.get(id=pk)

        self.check_object_permissions(request,d)

        s=TodoSerializer(d)

        return Response(s.data,status=status.HTTP_200_OK)

    def put(self,request,pk):

        d=Todo.objects.get(id=pk)

        self.check_object_permissions(request,d)

        s=TodoSerializer(instance=d,data=request.data)

        if s.is_valid():
            s.save()
            return Response(s.data,status=status.HTTP_201_CREATED)

        else:
            return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):

        d = Todo.objects.get(id=pk)

        self.check_object_permissions(request, d)

        s = TodoSerializer(instance=d, data=request.data, partial=True)

        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)

        else:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        d=Todo.objects.get(id=pk)

        self.check_object_permissions(request,d)

        d.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)