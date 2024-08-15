from django.contrib import admin

from DietPlan.Meal.models import Meal


# Register your models here.

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    display = ['pure_ai_response']
    fields = ['pure_ai_response']

    class Meta:
        model = Meal
