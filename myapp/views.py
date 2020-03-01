from django.shortcuts import render

# Create your views here.

import django_filters
from rest_framework import viewsets, filters

from myapp.models import User, Book
from myapp.serializers import UserSerializer, BookSerializer

# UserViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
