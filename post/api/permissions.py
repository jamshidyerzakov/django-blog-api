from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_admin)


class IsRightUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(bool(request.user == obj.author) or bool(request.user and request.user.is_admin))


class IsStaffUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)
