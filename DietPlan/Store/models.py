from django.db import models
from DietPlan.BodyTrait.models import BodyTrait

# Create your models here.
class Store(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    distance = models.FloatField(default=0.0)

    def __str__(self):
        return f'Store with price: {self.price}, distance: {self.distance} km'