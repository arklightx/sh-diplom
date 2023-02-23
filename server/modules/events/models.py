from django.db import models

from modules.home.models import Home


class Events(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    start = models.DateTimeField(verbose_name="Начало")
    end = models.DateTimeField(verbose_name="Конец")
    timed = models.BooleanField(blank=True, verbose_name="Завершено")
    description = models.TextField(verbose_name="Описание")
    home = models.ForeignKey(Home, on_delete=models.CASCADE, null=True, default=None, related_name="events", verbose_name="Дом")

    class Meta:
        verbose_name = "Ивент"
        verbose_name_plural = "Ивенты"

    def __str__(self) -> str:
        return f"{self.id}"

