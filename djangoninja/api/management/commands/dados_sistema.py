from django.core.management.base import BaseCommand
from django.db import transaction
from factory.django import DjangoModelFactory
from tests.factories.api.laboratorio_factory import LaboratorioFactory



import django

# Importe outras fábricas que você deseja usar
import logging

logger = logging.getLogger("django")


class Command(BaseCommand):
    help = "Cria dados de teste usando fábricas"

    def handle(self, *args, **kwargs):

        num_instances = 10  # Defina um número razoável para não sobrecarregar o DB
        try:
            laboratorios = LaboratorioFactory()
            print(f"Criando dados de teste... {laboratorios}")
        except Exception as e:
            logger.error(e)
            print(e)

    
        self.stdout.write(
            self.style.SUCCESS("Dados de teste foram criados com sucesso!")
        )