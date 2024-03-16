from typing import TYPE_CHECKING

from django.contrib.auth.models import AbstractUser
from django.db import models
from django_extensions.db.models import TimeStampedModel


if TYPE_CHECKING:  # pragma: no cover
    from SWM2024 import posts


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    observed_posts = models.ManyToManyField("posts.Post", through="UserObservedPost")

    def __str__(self):
        return self.username


class UserObservedPost(TimeStampedModel, models.Model):
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
    observer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.observer.username} - {self.post.title}"
