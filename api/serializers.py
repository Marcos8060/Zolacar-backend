from rest_framework import serializers
from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fiels = '__all__'


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Featured
        fiels = '__all__'