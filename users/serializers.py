from dataclasses import fields
from rest_framework import serializers, status
from core.exceptions import UniqueException
from users.models import User
from rest_framework.exceptions import APIException


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "date_joined",
            "updated_at",
        ]

    def validate_email(self, email: str):
        email_exists = User.objects.filter(email=email).exists()

        if email_exists:
            raise UniqueException(
                detail={"email": ["email already exists"]},
            )

        return email

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
