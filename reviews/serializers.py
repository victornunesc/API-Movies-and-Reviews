from django.shortcuts import get_object_or_404
from rest_framework import serializers
from movies.models import Movie

from reviews.models import Review
from users.models import User


class CriticsReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()


class ReviewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    stars = serializers.IntegerField(min_value=1, max_value=10)
    movie_id = serializers.PrimaryKeyRelatedField(read_only=True)
    critics = CriticsReviewSerializer(read_only=True, source="user_id")

    class Meta:
        model = Review
        exclude = ["user_id"]

    def create(self, validated_data):
        movie_id = validated_data.pop("movie_id")
        user_id = validated_data.pop("user")

        user = get_object_or_404(User, pk=user_id.id)
        movie = get_object_or_404(Movie, pk=movie_id)

        review = Review.objects.create(**validated_data, movie_id=movie, user_id=user)

        return review
