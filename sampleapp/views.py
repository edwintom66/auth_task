from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#from django.contrib.auth.models import MyUser
from .serializers import PanchayathSerializer,UserSerializer
from .models import Panchayath

from django.contrib.auth import get_user_model
User = get_user_model()

class PanchayathViewSet(viewsets.ModelViewSet):
    queryset = Panchayath.objects.all()
    serializer_class = PanchayathSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer