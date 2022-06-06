from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('cars/',CarList.as_view()),
    path('cars/<int:pk>/',CarDetail.as_view()),
    path('featured/',FeaturedList.as_view()),
    path('featured/<int:pk>/',FeatureDetail.as_view()),
    path('cars/search/',CarFleetDetailFilter.as_view()),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/',CustomUserCreate.as_view(),name='create_user'),
    path('logout/blacklist/',BlackListTokenView.as_view(),name='blacklist')
]