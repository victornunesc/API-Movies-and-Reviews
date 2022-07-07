from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status

from movies.serializers import MovieSerializer

# Create your views here.
class MovieViews(APIView):
    def post(self, request: Request):
        serialized = MovieSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()

        return Response(serialized.data, status.HTTP_201_CREATED)
