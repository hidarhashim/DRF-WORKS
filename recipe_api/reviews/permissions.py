from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    #object level permission
    def has_object_permission(selfself,request,view,obj):
        if request.method == 'GET':
            return True

        else:
            return obj.user == request.user


#if request method is GET returns True.

#here obj means review object

#condition obj.user==request.user checks whether the creator of object and requested user are same

#if yes returns True

#else returns false