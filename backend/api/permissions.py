from rest_framework.permissions import BasePermission


class IsOwnerOrderOrAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return (obj.user == request.user) or request.user.is_staff
