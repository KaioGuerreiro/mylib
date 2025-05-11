from rest_framework import serializers
from .models import Livro, ProgressoLeitura

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
        read_only_fields = ['usuario']

class ProgressoLeituraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressoLeitura
        fields = '__all__'
