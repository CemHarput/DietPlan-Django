
from django.contrib import admin

from DietPlan.Plan.models import Plan


# Register your models here.

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('diet_request', 'diet_start_date', 'diet_end_date')
    search_fields = ('diet_request', 'diet_start_date', 'diet_end_date')
    class Meta:
        model = Plan