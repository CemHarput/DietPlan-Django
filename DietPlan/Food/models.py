from django.db import models
from DietPlan.Meal.models import Meal


# Create your models here.
class Food(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='foods')
    calorie = models.FloatField()
    meal_time = models.TimeField()
    fat = models.FloatField()
    carb = models.FloatField()
    protein = models.FloatField()

    def __str__(self):
        return f"Food at {self.meal_time} - {self.calorie} cal"