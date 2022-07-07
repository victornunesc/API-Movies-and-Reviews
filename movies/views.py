from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from movies.models import Movie
from rest_framework.authentication import TokenAuthentication
from movies.permissions import MovieIdPermission, MoviePermission
from movies.serializers import MovieSerializer

# Create your views here.
class MovieViews(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MoviePermission]

    def post(self, request: Request):
        serialized = MovieSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()

        return Response(serialized.data, status.HTTP_201_CREATED)

    def get(self, _: Request):
        movies = Movie.objects.all()
        serialized = MovieSerializer(movies, many=True)

        return Response(serialized.data, status.HTTP_200_OK)


class MovieIdViews(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MovieIdPermission]

    def get(self, _: Request, movie_id):
        movie = Movie.objects.get(id=movie_id)
        serialized = MovieSerializer(movie)

        return Response(serialized.data, status.HTTP_200_OK)
