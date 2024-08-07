
from django.contrib import admin

from DietPlan.Ingredient.models import Ingredient
from DietPlan.Meal.models import Meal
from DietPlan.Plan.models import Plan


# Register your models here.

@admin.register(Ingredient)
class MealAdmin(admin.ModelAdmin):
    list_display = ('prep_time','cook_time','cost','ingredient_steps')
    search_fields = ('prep_time','cook_time','cost','ingredient_steps')
    class Meta:
        model = Ingredient