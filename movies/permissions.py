from rest_framework.permissions import BasePermission
from rest_framework.views import Request


class MoviePermission(BasePermission):
    def has_permission(self, request: Request, view):
        admin_methods = {"POST", "PATCH", "DELETE"}

        if request.method in admin_methods:
            return request.user.is_superuser

        return True


class MovieIdPermission(BasePermission):
    def has_permission(self, request: Request, view):
        admin_methods = {"PATCH", "DELETE"}

        if request.method in admin_methods:
            return request.user.is_superuser

        return True
