from django.shortcuts import render
from rest_framework import viewsets
from .models import Livro, ProgressoLeitura
from .serializers import LivroSerializer, ProgressoLeituraSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class ProgressoLeituraViewSet(viewsets.ModelViewSet):
    queryset = ProgressoLeitura.objects.all()
    serializer_class = ProgressoLeituraSerializer
