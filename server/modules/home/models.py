from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Home(models.Model):
    street = models.CharField(max_length=128)
    home_number = models.CharField(max_length=16)
    microdistrict = models.CharField(max_length=126)
    area = models.FloatField()
    create_dt = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.street} {self.home_number}"


class HomeLevel(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name="levels")
    level = models.IntegerField(null=False, default=0, blank=False)

    def __str__(self):
        return f"{self.home.street} {self.home.home_number}, этаж {self.level}"


class Apartment(models.Model):
    level = models.ForeignKey(HomeLevel, on_delete=models.CASCADE, related_name="apartments")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    apartment_number = models.IntegerField(null=False, default=0, blank=False)

    def __str__(self):
        return f"{self.level.home.street} {self.level.home.home_number}, этаж {self.level.level}, квартира {self.apartment_number}"


