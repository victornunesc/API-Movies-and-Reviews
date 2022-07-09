from django.urls import path
from reviews.views import MoviesIdReviewsViews, ReviewsIdViews, ReviewsViews


urlpatterns = [
    path("movies/<int:movie_id>/reviews/", MoviesIdReviewsViews.as_view()),
    path("reviews/<int:review_id>", ReviewsIdViews.as_view()),
    path("reviews/", ReviewsViews.as_view()),
]
