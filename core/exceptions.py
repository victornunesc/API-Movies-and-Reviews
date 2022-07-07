from rest_framework.exceptions import APIException
from rest_framework import status


class UniqueException(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "This value must be unique."
