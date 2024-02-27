from django.db import models
from api.models.laboratorio_model import Laboratorio


class GrupoDeServico(models.Model):
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='grupos_de_servico')
    nome = models.CharField(max_length=99, null=True, blank=True)
