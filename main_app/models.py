from django.db import models
from django.urls import reverse
# Create your models here.


class Character(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    element = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"character_id": self.id})
