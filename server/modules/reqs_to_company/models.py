from django.contrib.auth import get_user_model
from django.db import models

from modules.home.models import Home

User = get_user_model()


class Requests(models.Model):
    status = models.CharField(max_length=64, blank=True, verbose_name="Статус")
    create_dt = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    theme = models.CharField(max_length=256, verbose_name="Тема")
    text = models.TextField(verbose_name="Текст")
    done_dt = models.DateTimeField(null=True, blank=True, verbose_name="Дата выполнения")
    response = models.TextField(null=True, blank=True, verbose_name="Ответ")
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name="requests", verbose_name="Дом")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="От кого")

    class Meta:
        verbose_name = "Запрос"
        verbose_name_plural = "Запросы"

    def __str__(self):
        return f"Запрос №{self.id} для дома №{self.home.id}"
