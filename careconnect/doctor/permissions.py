from rest_framework.permissions import BasePermission


class IsAdminUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        if request.method == 'GET':
            return request.user.is_authenticated
        else:
            return request.user.is_authenticated and request.user.is_superuser

#GET -- should be Authenticated user

#POST/PUT/DELETE -- should be Authenticated+Admin user

#any admin can create/update/delete record