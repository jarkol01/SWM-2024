from datetime import timedelta

from django.utils import timezone
from djoser.views import UserViewSet
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet, ModelViewSet

from SWM2024.accounts.models import CustomUser


class CustomUserViewSet(UserViewSet):
    queryset = CustomUser.objects.all()


class UserObservedPostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
