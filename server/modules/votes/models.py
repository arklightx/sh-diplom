from django.contrib.auth import get_user_model
from django.db import models

from modules.home.models import Home

User = get_user_model()


class Votes(models.Model):
    theme = models.CharField(max_length=128, verbose_name="Название")
    home = models.ForeignKey(Home, on_delete=models.CASCADE, verbose_name="Дом")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель")
    isActive = models.BooleanField(default=False, blank=True, verbose_name="Активно")

    class Meta:
        verbose_name = "Голосование"
        verbose_name_plural = "Голосования"

    def __str__(self) -> str:
        return f"{self.id}. Дом: {self.home.id}. Тема: {self.theme}"


class VotesVariants(models.Model):
    label = models.CharField(max_length=128, verbose_name="Текст варианта")
    user = models.ManyToManyField(User, blank=True, verbose_name="Выбравшие этот вариант")
    for_vote = models.ForeignKey(Votes, on_delete=models.CASCADE, related_name="variants", verbose_name="Относится к голосованию")

    class Meta:
        verbose_name = "Вариант голосования"
        verbose_name_plural = "Варианты голосования"

    def __str__(self) -> str:
        return self.label
