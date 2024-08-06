from django.contrib import admin

from DietPlan.UserProfile.models import UserProfile


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('address', 'country', 'city')
    search_fields = ('address', 'country', 'city')
    class Meta:
        model = UserProfile
