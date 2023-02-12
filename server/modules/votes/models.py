from django.contrib.auth import get_user_model
from django.db import models

from modules.home.models import Home

User = get_user_model()


class Votes(models.Model):
    theme = models.CharField(max_length=128)
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=False, blank=True)


class VotesVariants(models.Model):
    label = models.CharField(max_length=128)
    user = models.ManyToManyField(User, blank=True)
    for_vote = models.ForeignKey(Votes, on_delete=models.CASCADE, related_name="variants")
