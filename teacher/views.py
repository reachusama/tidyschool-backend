from .serializers import *
from .models import *
from rest_framework import generics


# School
class SchoolList(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class SchoolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


# Class
class ClassList(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


# PersonalPlanner
class PersonalPlannerList(generics.ListCreateAPIView):
    queryset = PersonalPlanner.objects.all()
    serializer_class = PersonalPlannerSerializer


class PersonalPlannerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonalPlanner.objects.all()
    serializer_class = PersonalPlannerSerializer


# SupplyInventory
class SupplyInventoryList(generics.ListCreateAPIView):
    queryset = SupplyInventory.objects.all()
    serializer_class = SupplyInventorySerializer


class SupplyInventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupplyInventory.objects.all()
    serializer_class = SupplyInventorySerializer


# Subscription
class SubscriptionList(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class SubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
