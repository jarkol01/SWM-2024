from django.urls import include, path
from rest_framework import routers


app_name = "accounts"

urlpatterns = [
    path(r"", include("djoser.urls")),
    path(r"", include("djoser.urls.jwt")),
]

router = routers.DefaultRouter()

urlpatterns += router.urls
