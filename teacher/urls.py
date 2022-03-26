from django.urls import path, include
from .views import *

urlpatterns = [
    path('school/', SchoolList.as_view()),
    path('school/<int:pk>/', SchoolDetail.as_view()),

    path('class/', ClassList.as_view()),
    path('class/<int:pk>/', ClassDetail.as_view()),

    path('personal-planner/', PersonalPlannerList.as_view()),
    path('personal-planner/<int:pk>/', PersonalPlannerDetail.as_view()),

    path('supply-inventory/', SupplyInventoryList.as_view()),
    path('supply-inventory/<int:pk>/', SupplyInventoryDetail.as_view()),

    path('subscription/', SubscriptionList.as_view()),
    path('subscription/<int:pk>/', SubscriptionDetail.as_view()),
]
