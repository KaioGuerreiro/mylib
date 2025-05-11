from rest_framework import serializers
from .models import Livro, ProgressoLeitura

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class ProgressoLeituraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressoLeitura
        fields = '__all__'
