from django.urls import include, path
from rest_framework import routers

from SWM2024.posts.views import PostViewSet

app_name = "accounts"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet, "posts")

urlpatterns = router.urls
