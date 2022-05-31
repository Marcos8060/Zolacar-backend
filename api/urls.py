from django.urls import path
from .views import *

urlpatterns = [
    path('cars/',CarList.as_view()),
    path('cars/<int:pk>/',CarDetail.as_view()),
    path('featured/',FeaturedList.as_view()),
    path('featured/<int:pk>/',FeatureDetail.as_view()),
    path('cars/search/',CarFleetDetailFilter.as_view())
]