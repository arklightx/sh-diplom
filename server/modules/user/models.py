from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    patronymic = models.CharField(max_length=32, verbose_name="Отчество", default=None, blank=True, null=True)
    email = models.EmailField(verbose_name="Почта", unique=True)
    is_confirmed_email = models.BooleanField(default=False, verbose_name="Почта подтверждена?")
    token_email = models.TextField(verbose_name="Токен для подтверждения",
                                   null=True, blank=True, default=None)
    token_password_change = models.CharField(max_length=1024, verbose_name="Токен для замены пароля",
                                             null=True, blank=True, default=None)
    phone = models.CharField(max_length=15, verbose_name="Номер телефона", blank=True, null=True, default="Не указано")
    REQUIRED_FIELDS = ["password", "email"]
    USERNAME_FIELD = "username"

    class Meta:
        ordering = ["id"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        db_table = "pr_person"

    def __str__(self):
        return self.username


class AccessTokens(models.Model):
    token = models.TextField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valid_to = models.DateTimeField(default=None)

    class Meta:
        db_table = "pr_access_tokens"


class RefreshTokens(models.Model):
    token = models.TextField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valid_to = models.DateTimeField(default=None)
    access = models.OneToOneField(AccessTokens, on_delete=models.CASCADE)

    class Meta:
        db_table = "pr_refresh_tokens"
