from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Livro, ProgressoLeitura
from .serializers import LivroSerializer, ProgressoLeituraSerializer

class LivroViewSet(viewsets.ModelViewSet):
    serializer_class = LivroSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Livro.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class ProgressoLeituraViewSet(viewsets.ModelViewSet):
    serializer_class = ProgressoLeituraSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ProgressoLeitura.objects.filter(livro__usuario=self.request.user)
