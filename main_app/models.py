from django.db import models
from django.urls import reverse

EXPERIENCE = (
    ('HP', 'Hitpoints'),
    ('DE', 'Defense'),
    ('AT', 'Attack')
)


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


class Leveling(models.Model):
    date = models.DateField('leveled Up Date')
    exp = models.CharField(
        max_length=2,
        choices=EXPERIENCE,
        default=EXPERIENCE[0][0]
    )

    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_exp_display()} on {self.date}'

    class Meta:
        ordering = ['-date']
