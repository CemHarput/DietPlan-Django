import logging
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Meal
from .serializers import MealSerializer
from django.utils import timezone as now

logger = logging.getLogger(__name__)


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    def destroy(self, request, *args, **kwargs):
        # Log the delete attempt
        logger.info(f'[{now}] User {request.user} is attempting to delete Meal with ID {kwargs["pk"]}.')

        instance = self.get_object()
        self.perform_destroy(instance)

        logger.info(f'[{now}] User {request.user} successfully deleted Meal with ID {kwargs["pk"]}.')
        return Response(status=status.HTTP_204_NO_CONTENT)
