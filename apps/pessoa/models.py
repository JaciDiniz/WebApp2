from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    idade = models.IntegerField()

    def __str__(self):
       return f"Nome: {self.nome} ({self.sexo})"