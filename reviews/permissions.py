from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission

from reviews.models import Review


class MoviesIdReviewsPermissions(BasePermission):
    def has_permission(self, request, view):
        staff_methods = {"POST", "DELETE"}

        if request.method in staff_methods:
            return request.user.is_staff

        return True
