from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='livros')
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    total_paginas = models.IntegerField()
    ano_publicacao = models.IntegerField(null=True, blank=True)
    genero = models.CharField(max_length=100, null=True, blank=True)
    status_leitura = models.CharField(max_length=20, null=True, blank=True)
    nota = models.FloatField(default=0.0)

    def __str__(self):
        return self.titulo

class ProgressoLeitura(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='progresso')
    pagina_atual = models.IntegerField()
    data_atualizacao = models.DateTimeField(auto_now=True)
