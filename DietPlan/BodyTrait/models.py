from django.conf import settings
from django.db import models


# Create your models here.
class BodyTrait(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    weight = models.FloatField()
    height = models.FloatField()
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.get_gender_display()} - {self.weight}kg, {self.height}cm, {self.age} years"
