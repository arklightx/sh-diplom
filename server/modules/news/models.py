from django.db import models


class News(models.Model):
    title = models.CharField(max_length=256)
    create_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(upload_to="news")

    def __str__(self):
        return str(self.id)
