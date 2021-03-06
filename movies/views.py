from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView, Request, Response, status
from core.pagination import CustomPageNumberPagination
from movies.models import Movie
from rest_framework.authentication import TokenAuthentication
from movies.permissions import MovieIdPermission, MoviePermission
from movies.serializers import MovieSerializer

# Create your views here.
class MovieViews(APIView, CustomPageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MoviePermission]

    def post(self, request: Request):
        serialized = MovieSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()

        return Response(serialized.data, status.HTTP_201_CREATED)

    def get(self, request: Request):
        movies = Movie.objects.all()
        pagination = self.paginate_queryset(queryset=movies, request=request, view=self)
        serialized = MovieSerializer(pagination, many=True)

        return self.get_paginated_response(serialized.data)


class MovieIdViews(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MovieIdPermission]

    def get(self, _: Request, movie_id):
        movie = Movie.objects.get(id=movie_id)
        serialized = MovieSerializer(movie)

        return Response(serialized.data, status.HTTP_200_OK)

    def patch(self, request: Request, movie_id):
        movie = get_object_or_404(
            Movie,
            pk=movie_id,
        )
        serialized = MovieSerializer(instance=movie, data=request.data, partial=True)
        serialized.is_valid(raise_exception=True)
        serialized.save()

        return Response(serialized.data, status.HTTP_200_OK)

    def delete(self, _: Request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        movie.delete()

        return Response("", status.HTTP_204_NO_CONTENT)
