from django.db import models

# Create your models here.


class Character(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    element = models.CharField(max_length=100)

    def __str__(self):
        return self.name
