from django.db import models


class Question(models.Model):
    question = models.TextField(verbose_name="Вопрос")
    answer = models.TextField(null=True, blank=True, verbose_name="Ответ")
    theme = models.CharField(max_length=32, verbose_name="Тема", blank=True, null=True, default=None)
    author_email = models.CharField(max_length=64)

    class Meta:
        ordering = ["id"]
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.question
