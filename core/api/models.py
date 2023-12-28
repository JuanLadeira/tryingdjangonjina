from django.db import models

# Create your models here.


class Laboratorio(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    endereco = models.CharField(max_length=100, null=True, blank=True)
    status = models.BooleanField(default=True)
    numero_da_acreditacao = models.IntegerField(null=True, blank=True)
    situacao = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    UF = models.CharField(max_length=100, null=True, blank=True)

    gerente = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nome