from django.db import models


class News(models.Model):
    title = models.CharField(max_length=256, verbose_name="Тайтл")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    description = models.TextField(verbose_name="Текст новости")
    image = models.ImageField(upload_to="news", verbose_name="Изображение")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return str(self.id)
