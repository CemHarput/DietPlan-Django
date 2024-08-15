import logging
from openai import OpenAI
from rest_framework import viewsets, filters, status
from datetime import datetime

from rest_framework.response import Response

from DietPlan.Meal.serializers import MealSerializer
from DietPlan.Plan.models import Plan
from DietPlan.Plan.serializers import PlanSerializer
import environ

logger = logging.getLogger(__name__)
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
env = environ.Env(DEBUG=(bool,  False))
environ.Env.read_env()

client = OpenAI(
    organization=env('OPENAI_ORG'),
    api_key=env('OPENAI_SECRETKEY')
)


def log_creation_attempt(user):
    logger.info(f'[{now}] User {user} is attempting to create a Plan.')


def extract_plan_data(request):
    return {
        'diet_request': request.data.get('diet_request'),
        'body_trait': request.data.get('body_trait'),
        'diet_start_date': request.data.get('diet_start_date'),
        'diet_end_date': request.data.get('diet_end_date'),
    }


def call_chatgpt_for_meal_suggestion(plan):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"""
            Based on the following information:
            BodyTrait: {plan.body_trait},
            Diet Start Date: {plan.diet_start_date},
            Diet End Date: {plan.diet_end_date},
            User's diet request: {plan.diet_request},
            Please suggest a detailed meal plan.
        """}
    ]

    chatgpt_response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=150
    )
    return chatgpt_response.choices[0].message.content.strip()


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['diet_request']
    ordering_fields = ['diet_start_date', 'diet_end_date']

    def create_plan(self, plan_data):
        plan_serializer = self.get_serializer(data=plan_data)
        plan_serializer.is_valid(raise_exception=True)
        return plan_serializer.save()

    def create_meal(self, plan, meal_suggestion):
        meal_data = {
            'plan': plan.id,
            'pure_ai_response': meal_suggestion
        }

        meal_serializer = MealSerializer(data=meal_data)
        meal_serializer.is_valid(raise_exception=True)
        meal_serializer.save()

    def create(self, request, *args, **kwargs):

        log_creation_attempt(request.user)
        plan_data = extract_plan_data(request)
        plan = self.create_plan(plan_data)
        meal_suggestion = call_chatgpt_for_meal_suggestion(plan)
        self.create_meal(plan, meal_suggestion)
        logger.info(f'[{now}] User {request.user} successfully created Plan with ID {plan.id} and associated Meal.')
        return Response(self.get_serializer(plan).data, status=status.HTTP_201_CREATED)

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
