from django.db import models
from DietPlan.BaseModel.BaseModel import BaseModel
from DietPlan.Plan.models import Plan


# Create your models here.
class Food(BaseModel):
    calorie = models.FloatField()
    meal_time = models.TimeField()
    fat = models.FloatField()
    carb = models.FloatField()
    protein = models.FloatField()

    def __str__(self):
        return f"Food at {self.meal_time} - {self.calorie} cal"