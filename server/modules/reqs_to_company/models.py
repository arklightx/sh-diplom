from django.contrib.auth import get_user_model
from django.db import models

from modules.home.models import Home

User = get_user_model()


class Requests(models.Model):
    status = models.CharField(max_length=64, blank=True)
    create_dt = models.DateTimeField(auto_now_add=True)
    theme = models.CharField(max_length=256)
    text = models.TextField()
    done_dt = models.DateTimeField(null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name="requests")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Запрос №{self.id} для дома №{self.home.id}"
