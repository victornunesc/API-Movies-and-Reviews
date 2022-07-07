from dataclasses import field
from rest_framework import serializers

from movies.models import Genre, Movie


class GenreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def create(self, validated_data):
        genres = validated_data.pop("genres")

        movie = Movie.objects.create(**validated_data)

        for genre in genres:
            genre, _ = Genre.objects.get_or_create(name=genre["name"])
            movie.genres.add(genre)

        return movie
