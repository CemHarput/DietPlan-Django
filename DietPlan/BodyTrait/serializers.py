from rest_framework import serializers
from .models import BodyTrait


class BodyTraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyTrait
        fields = '__all__'
