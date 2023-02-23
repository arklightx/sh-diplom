from django.db import models
from modules.home.models import Apartment, Home


class Document(models.Model):
    type = models.CharField(max_length=120, verbose_name="Тип документа")
    title = models.CharField(max_length=200, verbose_name="Тайтл")
    file = models.FileField(upload_to="documents", verbose_name="Файл")
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name="documents", verbose_name="Дом")

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self) -> str:
        return f"{self.id} {self.type}"



class Disablings(models.Model):
    status = models.CharField(max_length=60, verbose_name="Статус")
    resource = models.CharField(max_length=60, verbose_name="Отключаемый ресурс")
    reason = models.CharField(max_length=60, verbose_name="Причина отключения")
    disable_dt = models.DateTimeField(verbose_name="Дата отключения")
    enable_dt = models.DateTimeField(verbose_name="Дата включения")
    fact_dt = models.DateTimeField(null=True, blank=True, verbose_name="Фактическая дата включения")
    aparment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name="disablings", verbose_name="Квартира")

    class Meta:
        verbose_name = "Отключение"
        verbose_name_plural = "Отключения"

    def __str__(self) -> str:
        return f"{self.id}"
