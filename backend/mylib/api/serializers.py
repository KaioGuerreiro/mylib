from rest_framework import serializers
from .models import Livro, ProgressoLeitura
from django.contrib.auth.models import User

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
        read_only_fields = ['usuario']

class ProgressoLeituraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressoLeitura
        fields = '__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user