from django.db import models
from DietPlan.Meal.models import Meal


# Create your models here.
class Ingredient(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='ingredients')
    prep_time = models.TimeField()
    cook_time = models.TimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    ingredient_steps = models.TextField()

    def __str__(self):
        return f"Ingredient for meal at {self.prep_time}"