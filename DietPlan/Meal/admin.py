
from django.contrib import admin

from DietPlan.Meal.models import Meal
from DietPlan.Plan.models import Plan


# Register your models here.

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('plan','meal_time')
    search_fields = ('plan','meal_time')
    class Meta:
        model = Meal