from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10)
    premiere = models.DateField()
    classification = models.IntegerField()
    synopsis = models.TextField()

    genres = models.ManyToManyField(to="movies.Genre")


class Genre(models.Model):
    name = models.CharField(max_length=127)
