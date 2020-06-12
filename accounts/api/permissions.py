from rest_framework.permissions import BasePermission


class IsRightUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(bool(request.user == obj) or bool(request.user and request.user.is_admin))