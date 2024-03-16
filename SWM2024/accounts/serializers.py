from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from SWM2024.accounts.models import CustomUser


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "phone_number",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "avatar",
        ]


class UserObservedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser.observed_posts.through
        fields = "__all__"
