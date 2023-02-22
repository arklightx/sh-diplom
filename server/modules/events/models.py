from django.db import models

from modules.home.models import Home


class Events(models.Model):
    name = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()
    timed = models.BooleanField(blank=True)
    description = models.TextField()
    home = models.ForeignKey(Home, on_delete=models.CASCADE, null=True, default=None, related_name="events")

