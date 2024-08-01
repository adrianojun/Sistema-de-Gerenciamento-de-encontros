# models.py
from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    bairro = models.TextField(max_length=255)
    sexo = models.TextField(max_length=10)
    cidade = models.TextField(max_length=255)

class Encontro(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='encontros')
    data = models.DateTimeField()
    horario = models.TimeField(default='00:00')
    descricao = models.TextField()

    def __str__(self):
        return f"{self.usuario.nome} - {self.data.strftime('%Y-%m-%d %H:%M')}"
