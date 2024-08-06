from django.contrib import admin

import DietPlan
from DietPlan.BodyTrait.models import BodyTrait


# Register your models here.
@admin.register(BodyTrait)
class BodyTraitAdmin(admin.ModelAdmin):
    class Meta:
        model = BodyTrait