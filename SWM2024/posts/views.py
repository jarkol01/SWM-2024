from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from SWM2024.accounts.models import UserObservedPost


class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["post"])
    def observe(self, request):
        user = request.user
        UserObservedPost.objects.get_or_create(user=user)
        return Response(status=201)
