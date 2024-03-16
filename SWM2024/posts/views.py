from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from SWM2024.accounts.models import UserObservedPost
from SWM2024.posts.models import Post
from SWM2024.posts.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    @action(detail=True, methods=["post"])
    def observe(self, request):
        user = request.user
        UserObservedPost.objects.get_or_create(user=user)
        return Response(status=201)
