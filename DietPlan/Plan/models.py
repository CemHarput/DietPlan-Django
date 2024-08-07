from django.db import models
from DietPlan.BaseModel.BaseModel import BaseModel
from DietPlan.BodyTrait.models import BodyTrait



# Create your models here.
class Plan(BaseModel):
    body_trait = models.ForeignKey(BodyTrait, on_delete=models.CASCADE, related_name='plans')
    diet_request = models.TextField()
    diet_start_date = models.DateField()
    diet_end_date = models.DateField()

    def __str__(self):
        return f"Plan from {self.diet_start_date} to {self.diet_end_date}"