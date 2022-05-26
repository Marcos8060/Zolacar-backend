from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *

# Create your views here.
class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetail(generics.RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class FeaturedList(generics.ListCreateAPIView):
    queryset = Featured.objects.all()
    serializer_class = FeatureSerializer

class FeatureDetail(generics.RetrieveUpdateAPIView):
    queryset = Featured.objects.all()
    serializer_class = FeatureSerializer

