from django.db import models
from .utils import generate_short


class Link(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    url = models.CharField(max_length=1000, blank=False)
    short = models.CharField(max_length=10, default=generate_short)

    def __str__(self):
        return self.short
