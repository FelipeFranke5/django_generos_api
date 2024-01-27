from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=128, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
