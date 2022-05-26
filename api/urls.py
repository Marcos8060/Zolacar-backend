from django.urls import path
from .views import *

urlpatterns = [
    path('cars/',CarList.as_view()),
    path('featured/',FeaturedList.as_view()),
]