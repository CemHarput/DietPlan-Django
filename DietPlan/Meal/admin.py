
from django.contrib import admin

from DietPlan.Meal.models import Meal

# Register your models here.

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    display = ['meal_time']
    fields = ['meal_time']
    class Meta:
        model = Meal