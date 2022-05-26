from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *

# Create your views here.
class CarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class FeaturedList(generics.ListAPIView):
    queryset = Featured.objects.all()
    serializer_class = FeatureSerializer

