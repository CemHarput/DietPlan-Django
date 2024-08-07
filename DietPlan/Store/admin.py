
from django.contrib import admin

from DietPlan.Store.models import Store


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    class Meta:
        model = Store