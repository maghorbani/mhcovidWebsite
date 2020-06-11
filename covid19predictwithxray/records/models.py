from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    file = models.FileField(blank=False, null=False)
    score = models.FloatField(null=True, blank=True)
    owner = models.ForeignKey(
        User, related_name="images", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
