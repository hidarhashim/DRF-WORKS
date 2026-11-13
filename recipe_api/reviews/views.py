from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from reviews.serializers import ReviewSerializer

from reviews.permissions import IsOwner


# Create your views here.
class CreateReview(APIView):

    authentication_classes = [BasicAuthentication,]
    permission_classes = [IsAuthenticated,]

    def post(self,request):

        u=request.user#current requested user

        s=ReviewSerializer(data=request.data) #data contains only comment,rating and recipe ,user not included
        if s.is_valid():
            s.save(user=u)
            return Response(s.data,status=status.HTTP_201_CREATED)
        else:
            return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)

#apiview for reading all review of a specifc recipe

from reviews.models import Review
class ReadReview(APIView):
    authentication_classes = [BasicAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self,request,pk):
        r=Review.objects.filter(recipe=pk)
        s=ReviewSerializer(r,many=True)
        return Response(s.data,status=status.HTTP_200_OK)

#apiview for updating a review
class ReviewUpdate(APIView):
    authentication_classes = [BasicAuthentication, ]
    permission_classes = [IsAuthenticated,IsOwner ]

    def put(self,request,pk):
        e=request.data
        r=Review.objects.get(id=pk)

        self.check_object_permissions(request,r) #manually checks whether the requested user -
        #- has the permission to perform operation on the review object r

        s=ReviewSerializer(instance=r,data=e)
        if s.is_valid():
            s.save()
            return Response(s.data,status=status.HTTP_201_CREATED)
        else:
            return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)

#apiview for deleting a review

class ReviewDelete(APIView):
    authentication_classes = [BasicAuthentication, ]
    permission_classes = [IsAuthenticated,IsOwner ]
    def delete(self,request,pk):
        r=Review.objects.get(id=pk)

        self.check_object_permissions(request, r)  # manually checks whether the requested user -
        # - has the permission to perform operation on the review object r

        r.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)