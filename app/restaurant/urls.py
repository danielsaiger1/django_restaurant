"""
URL mappings for the restaurant app
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from restaurant import views


router = DefaultRouter()
router.register('restaurants', views.RestaurantViewSet)
router.register('tags', views.TagViewSet)


app_name = 'restaurant'

urlpatterns = [
    path('', include(router.urls)),
]
