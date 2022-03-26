from rest_framework import serializers
from .models import *


class SchoolSerializer(serializers.Serializer):
    class Meta:
        model = School
        fields = '__all__'


class ClassSerializer(serializers.Serializer):
    class Meta:
        model = Class
        fields = '__all__'


class PersonalPlannerSerializer(serializers.Serializer):
    class Meta:
        model = PersonalPlanner
        fields = '__all__'


class SupplyInventorySerializer(serializers.Serializer):
    class Meta:
        model = SupplyInventory
        fields = '__all__'


class SubscriptionSerializer(serializers.Serializer):
    class Meta:
        model = Subscription
        fields = '__all__'
