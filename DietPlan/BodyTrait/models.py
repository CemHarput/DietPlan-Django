from django.db import models
from DietPlan.BaseModel.BaseModel import BaseModel


# Create your models here.
class BodyTrait(BaseModel):
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
