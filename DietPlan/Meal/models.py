from django.core.validators import MaxLengthValidator
from django.db import models
from DietPlan.Plan.models import Plan


# Create your models here.
class Meal(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='meals')
    pure_ai_response = models.TextField(validators=[MaxLengthValidator(10000)])

    def __str__(self):
        return f"Meal at {self.pure_ai_response}"
