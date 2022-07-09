from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from reviews.models import Review
from reviews.permissions import MoviesIdReviewsPermissions

from reviews.serializers import ReviewSerializer

from rest_framework.authentication import TokenAuthentication


class MoviesIdReviewsViews(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MoviesIdReviewsPermissions]

    def post(self, request: Request, movie_id):
        serialized = ReviewSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save(user=request.user, movie_id=movie_id)

        return Response(serialized.data, status.HTTP_201_CREATED)

    def get(self, _: Request, movie_id):
        reviews = Review.objects.filter(movie_id=movie_id)
        serialized = ReviewSerializer(reviews, many=True)

        return Response(serialized.data, status.HTTP_200_OK)


class ReviewsIdViews(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MoviesIdReviewsPermissions]

    def delete(self, request: Request, review_id):
        review = get_object_or_404(Review, pk=review_id)

        if review.user_id != request.user.id and not request.user.is_superuser:
            return Response(
                {"message": "You need to owner the review"}, status.HTTP_403_FORBIDDEN
            )

        review.delete()

        return Response("", status.HTTP_204_NO_CONTENT)


class ReviewsViews(APIView):
    def get(self, _: Request):
        reviews = Review.objects.all()
        serialized = ReviewSerializer(reviews, many=True)

        return Response(serialized.data, status.HTTP_200_OK)
