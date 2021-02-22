from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import PanchayathViewSet,UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

router.register('panchayath', PanchayathViewSet)

urlpatterns = [
    path('', include(router.urls)),
]