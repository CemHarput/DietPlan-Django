from django.apps import AppConfig


class DietPlanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    update_date = 'django.db.models.DateTimeField(auto_now_add=True)'
    creation_date = 'django.db.models.DateTimeField(blank=True, auto_now_add=True)'
    name = 'DietPlan'
