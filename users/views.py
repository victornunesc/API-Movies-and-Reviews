from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status

from users.serializers import UserSerializer


# Create your views here.
class UserView(APIView):
    def post(self, request: Request):
        serialized = UserSerializer(data=request.data)

        serialized.is_valid(raise_exception=True)
        serialized.save()

        return Response(serialized.data, status.HTTP_201_CREATED)
