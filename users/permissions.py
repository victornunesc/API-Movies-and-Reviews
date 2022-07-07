from rest_framework.permissions import BasePermission
from rest_framework.views import Request


class UserPermission(BasePermission):
    def has_permission(self, request: Request, view):
        admin_methods = {"GET"}

        if request.method in admin_methods:
            return request.user.is_superuser

        return True


class UserIdPermission(BasePermission):
    def has_permission(self, request: Request, view):
        admin_methods = {"GET"}

        if request.method in admin_methods:
            return request.user.is_superuser

        return True
