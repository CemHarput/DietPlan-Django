from django.contrib import admin

from DietPlan.UserProfile.models import UserProfile


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = UserProfile
