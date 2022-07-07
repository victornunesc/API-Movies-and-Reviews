from django.urls import path

from movies.views import MovieIdViews, MovieViews


urlpatterns = [
    path("movies/", MovieViews.as_view()),
    path("movies/<movie_id>", MovieIdViews.as_view()),
]
