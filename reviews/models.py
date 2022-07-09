from django.db import models


class RecomendationChoices(models.TextChoices):
    MUST = "Must Watch"
    SHOULD = "Should Watch"
    AVOID = "Avoid Watch"
    NO_OPINION = "No Opinion"


class Review(models.Model):
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField()
    recomendation = models.CharField(
        max_length=50,
        null=True,
        choices=RecomendationChoices.choices,
        default=RecomendationChoices.NO_OPINION,
    )

    movie_id = models.ForeignKey(
        to="movies.Movie", related_name="reviews", on_delete=models.SET_NULL, null=True
    )
    user_id = models.ForeignKey(
        to="users.User", related_name="reviews", on_delete=models.SET_NULL, null=True
    )
