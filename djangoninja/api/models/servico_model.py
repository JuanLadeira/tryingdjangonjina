from django.db import models
from api.models.grupo_de_servico_model import GrupoDeServico

class Servico(models.Model):
    grupo = models.ForeignKey(GrupoDeServico, on_delete=models.CASCADE, related_name='servicos')
    descricao = models.CharField(max_length=100, null=True, blank=True)
    metodo = models.CharField(max_length=100, null=True, blank=True)
    cmc = models.CharField(max_length=100, null=True, blank=True)