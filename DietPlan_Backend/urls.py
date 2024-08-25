"""
URL configuration for DietPlan_Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from DietPlan.BodyTrait.views import BodyTraitViewSet
from DietPlan.Meal.views import MealViewSet
from DietPlan.Plan.views import PlanViewSet

router = DefaultRouter()
router.register(r'bodytraits', BodyTraitViewSet)
router.register(r'plans', PlanViewSet)
router.register(r'meals', MealViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # DRF login/logout
    path('', include(router.urls)),
]
