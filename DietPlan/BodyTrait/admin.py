from django.contrib import admin

import DietPlan
from DietPlan.BodyTrait.models import BodyTrait


# Register your models here.
@admin.register(BodyTrait)
class BodyTraitAdmin(admin.ModelAdmin):
    list_display = ('gender', 'weight', 'height','age')
    search_fields = ('gender', 'weight', 'height','age')
    class Meta:
        model = BodyTrait