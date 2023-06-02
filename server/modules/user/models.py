from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    patronymic = models.CharField(max_length=32, verbose_name="Отчество", default=None, blank=True, null=True)
    email = models.EmailField(verbose_name="Почта", unique=True)
    phone = models.CharField(max_length=15, verbose_name="Номер телефона", blank=True, null=True, default="Не указано")
    REQUIRED_FIELDS = ["password", "email"]
    USERNAME_FIELD = "username"

    class Meta:
        ordering = ["id"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username


class AccessTokens(models.Model):
    token = models.TextField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valid_to = models.DateTimeField(default=None)


class RefreshTokens(models.Model):
    token = models.TextField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valid_to = models.DateTimeField(default=None)
    access = models.OneToOneField(AccessTokens, on_delete=models.CASCADE)

