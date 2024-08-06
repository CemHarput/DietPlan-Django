from django.db import models
from DietPlan.BaseModel.BaseModel import BaseModel
from DietPlan.Plan.models import Plan


# Create your models here.
class Meal(BaseModel):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='meals')
    meal_time = models.TimeField()

    def __str__(self):
        return f"Meal at {self.meal_time} for plan {self.plan}"