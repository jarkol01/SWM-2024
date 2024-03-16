from django.urls import include, path
from rest_framework import routers

from SWM2024.accounts.views import UserObservedPostViewSet

app_name = "accounts"

urlpatterns = [
    path(r"", include("djoser.urls")),
    path(r"", include("djoser.urls.jwt")),
]

router = routers.DefaultRouter()
router.register(r"user_observed_post", UserObservedPostViewSet, "user_observed_post")

urlpatterns += router.urls
