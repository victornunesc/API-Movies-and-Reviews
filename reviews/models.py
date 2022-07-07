from django.db import models


class Review(models.Model):
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField()
    recomendation = models.CharField(max_length=50)

    movie_id = models.ForeignKey(
        to="movies.Movie", related_name="reviews", on_delete=models.SET_NULL, null=True
    )
    user_id = models.ForeignKey(
        to="users.User", related_name="reviews", on_delete=models.SET_NULL, null=True
    )
