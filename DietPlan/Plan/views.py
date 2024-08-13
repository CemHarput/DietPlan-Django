import logging
import openai
from rest_framework import viewsets, filters, status
from datetime import datetime

from rest_framework.response import Response

from DietPlan.Meal.serializers import MealSerializer
from DietPlan.Plan.models import Plan
from DietPlan.Plan.serializers import PlanSerializer

logger = logging.getLogger(__name__)
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['diet_request']
    ordering_fields = ['diet_start_date', 'diet_end_date']

    def create(self, request, *args, **kwargs):
        logger.info(f'[{now}] User {request.user} is attempting to create a Plan.')

        # Extract the data needed to create a Plan
        plan_data = {
            'diet_request': request.data.get('diet_request'),
            'body_trait': request.data.get('body_trait'),
            'diet_start_date': request.data.get('diet_start_date'),
            'diet_end_date': request.data.get('diet_end_date'),
        }

        # Create and save the Plan entity
        plan_serializer = self.get_serializer(data=plan_data)
        plan_serializer.is_valid(raise_exception=True)
        plan = plan_serializer.save()

        # Formulate the prompt for ChatGPT based on the Plan data
        prompt = f"""
        Based on the following information:
        BodyTrait: {plan.body_trait},
        Diet Start Date: {plan.diet_start_date},
        Diet End Date: {plan.diet_end_date},
        User's diet request: {plan.diet_request},
        Please suggest a detailed meal plan.
        """

        # Call ChatGPT API to get meal suggestions
        chatgpt_response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )

        # Extract the response text
        meal_suggestion = chatgpt_response.choices[0].text.strip()

        # Create and save the Meal entity with the response from ChatGPT
        meal_data = {
            'plan': plan.id,
            'meal_time': plan.diet_start_date,  # You may want to adjust this
            'pure_ai_response': meal_suggestion
        }

        # Assuming you have a MealSerializer to handle Meal creation
        meal_serializer = MealSerializer(data=meal_data)
        meal_serializer.is_valid(raise_exception=True)
        meal_serializer.save()

        logger.info(f'[{now}] User {request.user} successfully created Plan with ID {plan.id} and associated Meal.')

        # Return the Plan's serialized data
        return Response(plan_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        logger.info(f'[{now}] User {request.user} is attempting to update Plan with ID {kwargs["pk"]}.')
        response = super().update(request, *args, **kwargs)
        if response.status_code in [status.HTTP_200_OK, status.HTTP_204_NO_CONTENT]:
            logger.info(f'[{now}] User {request.user} successfully updated Plan with ID {kwargs["pk"]}.')
        return response

    def destroy(self, request, *args, **kwargs):
        logger.info(f'[{now}] User {request.user} is attempting to delete Plan with ID {kwargs["pk"]}.')
        response = super().destroy(request, *args, **kwargs)
        if response.status_code == status.HTTP_204_NO_CONTENT:
            logger.info(f'[{now}] User {request.user} successfully deleted Plan with ID {kwargs["pk"]}.')
        return response

