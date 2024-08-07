
from django.contrib import admin

from DietPlan.Food.models import Food
from DietPlan.Meal.models import Meal


# Register your models here.

@admin.register(Food)
class MealAdmin(admin.ModelAdmin):
    list_display = ('calorie','meal_time','fat','carb','protein')
    search_fields = ('calorie','meal_time','fat','carb','protein')
    class Meta:
        model = Food