import uuid
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Home(models.Model):
    street = models.CharField(max_length=128, verbose_name="Улица")
    home_number = models.CharField(max_length=16, verbose_name="Номер дома")
    microdistrict = models.CharField(max_length=126, verbose_name="Микрорайон")
    area = models.FloatField(verbose_name="Площадь")
    create_dt = models.DateTimeField(verbose_name="Дата основания")
    is_deleted = models.BooleanField(default=False, verbose_name="Удалён из системы")
    users = models.ManyToManyField(User, related_name="homes", verbose_name="Жильцы")
    jitsi = models.CharField(max_length=128, blank=True, null=False, default=uuid.uuid4(), unique=True, verbose_name="GUID конференции")
    messanger_link = models.CharField(max_length=1000, blank=True, null=True, verbose_name="Ссылка на мессенджер")

    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "Дома"

    def __str__(self):
        return f"{self.street} {self.home_number}"


class HomeLevel(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name="levels", verbose_name="Дом")
    level = models.IntegerField(null=False, default=0, blank=False, verbose_name="Этаж")

    class Meta:
        verbose_name = "Этаж"
        verbose_name_plural = "Этажи"

    def __str__(self):
        return f"{self.home.street} {self.home.home_number}, этаж {self.level}"


class Apartment(models.Model):
    level = models.ForeignKey(HomeLevel, on_delete=models.CASCADE, related_name="apartments", verbose_name="Этаж")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Жилец")
    apartment_number = models.IntegerField(null=False, default=0, blank=False, verbose_name="Номер квартиры")

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"

    def __str__(self):
        return f"{self.level.home.street} {self.level.home.home_number}, этаж {self.level.level}, квартира {self.apartment_number}"


class Staff(models.Model):
    first_name = models.CharField(max_length=70, verbose_name="Имя")
    last_name = models.CharField(max_length=70, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=70, verbose_name="Отчество")
    role = models.CharField(max_length=50, verbose_name="Должность")
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name="staffs", verbose_name="Дом")

    class Meta:
        verbose_name = "Персонал"
        verbose_name_plural = "Персонал"

    def __str__(self) -> str:
        return f"{self.id}. Дом - {self.home.id}"
