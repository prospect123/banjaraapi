from .serializers import TermsconSerializer
from django.shortcuts import render
from .models import term_cond
from rest_framework import viewsets

class ccondModelViewSet(viewsets.ModelViewSet):
    queryset = term_cond.objects.all()
    serializer_class = TermsconSerializer