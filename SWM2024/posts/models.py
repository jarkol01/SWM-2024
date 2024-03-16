from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel


CustomUser = get_user_model()


class Post(TimeStampedModel, models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    issuer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title



