from django.db import models
from modules.home.models import Apartment, Home


class Document(models.Model):
    type = models.CharField(max_length=120)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="documents")
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name="documents")


class Disablings(models.Model):
    status = models.CharField(max_length=60)
    resource = models.CharField(max_length=60)
    reason = models.CharField(max_length=60)
    disable_dt = models.DateTimeField()
    enable_dt = models.DateTimeField()
    fact_dt = models.DateTimeField(null=True, blank=True)
    aparment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name="disablings")