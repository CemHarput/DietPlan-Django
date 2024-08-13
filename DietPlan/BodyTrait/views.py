import logging
from rest_framework import viewsets, filters, status
from datetime import datetime
from rest_framework.response import Response

from DietPlan.BodyTrait.models import BodyTrait
from DietPlan.BodyTrait.serializers import BodyTraitSerializer

logger = logging.getLogger(__name__)
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Create your views here.
class BodyTraitViewSet(viewsets.ModelViewSet):
    queryset = BodyTrait.objects.all()
    serializer_class = BodyTraitSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['gender']
    ordering_fields = ['weight', 'height', 'age']

    def create(self, request, *args, **kwargs):
        logger.info(f"[{now}] User {request.user} is attempting to create a BodyTrait.")
        user = request.user
        if BodyTrait.objects.filter(user=user).exists():
            logger.error(f"[{now}] {request.user} can only have one BodyTrait.")
            return Response({"error": "You can only have one BodyTrait."}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        logger.info(f"[{now}] User {request.user} is attempting to update BodyTrait with ID {kwargs['pk']}")
        response = super().update(request, *args, **kwargs)
        if response.status_code in [status.HTTP_200_OK, status.HTTP_204_NO_CONTENT]:
            logger.info(f"[{now}] User {request.user} successfully updated BodyTrait with ID {kwargs['pk']}")
        return response

    def destroy(self, request, *args, **kwargs):
        logger.info(f"[{now}] User {request.user} is attempting to delete BodyTrait with ID {kwargs['pk']}")
        response = super().destroy(request, *args, **kwargs)
        if response.status_code == status.HTTP_204_NO_CONTENT:
            logger.info(f"[{now}] User {request.user} successfully deleted BodyTrait with ID {kwargs['pk']}")
        return response
