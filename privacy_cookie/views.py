from .serializers import CookieSerializer
from django.shortcuts import render
from .models import cookies
from rest_framework import viewsets

class CookieModelViewSet(viewsets.ModelViewSet):
    queryset = cookies.objects.all()
    serializer_class = CookieSerializer