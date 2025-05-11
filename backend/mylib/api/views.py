from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, status
from .models import Livro, ProgressoLeitura
from .serializers import LivroSerializer, ProgressoLeituraSerializer, UserCreateSerializer

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

class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuário criado com sucesso"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)