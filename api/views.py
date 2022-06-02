from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *
from rest_framework import filters
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


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


class CarFleetDetailFilter(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=brand']  #exact match search
    # ['^slug'] starts-with search functionality
    # ['@']  full text search works best with postgresql
    # ['$']  regex search

