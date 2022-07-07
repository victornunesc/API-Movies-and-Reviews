from django.urls import path

from movies.views import MovieViews


urlpatterns = [path("movies/", MovieViews.as_view())]
