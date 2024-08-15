from django.db import models
from DietPlan.BodyTrait.models import BodyTrait


# Create your models here.
class Plan(models.Model):
    body_trait = models.ForeignKey(BodyTrait, on_delete=models.CASCADE, related_name='plans')
    diet_request = models.TextField()
    diet_start_date = models.DateField()
    diet_end_date = models.DateField()
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Plan from {self.diet_start_date} to {self.diet_end_date}"
