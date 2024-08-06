from django.db import models
from django.contrib.auth.models import User
from DietPlan.BodyTrait.models import BodyTrait


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    body_trait = models.OneToOneField(BodyTrait, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username