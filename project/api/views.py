from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth.models import GroupManager
from rest_framework import viewsets
from project.api.serializers import UserSerializer
from project.api.serializers import DerrickSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

