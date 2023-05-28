from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=80, verbose_name="Компания")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
    

class CompanyServices(models.Model):
    price = models.FloatField()
    service_name = models.CharField(max_length=512, null=False, verbose_name="Услуга")
    group = models.CharField(max_length=150, verbose_name="Группирующее наименование")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Компания", null=True, blank=True, related_name="services")

    def __str__(self) -> str:
        return f"\"{self.company.name}\". {self.service_name}"

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

