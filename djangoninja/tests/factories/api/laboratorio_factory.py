import factory
from api.models.laboratorio_model import Laboratorio


class LaboratorioFactory(factory.Factory):
    class Meta:
        model = Laboratorio

    nome = factory.Sequence(lambda n: f"laboratorio_{n}")
    endereco = factory.Sequence(lambda n: f"endereco_{n}")
    telefone = factory.Faker('phone_number')
    email = factory.Faker('email')
    status = True
    numero_da_acreditacao = factory.Sequence(lambda n: float(f"{n:2f}"))
    situacao = factory.Sequence(lambda n: f"situacao_{n}")
    bairro = factory.Sequence(lambda n: f"bairro_{n}")
    cidade = factory.Sequence(lambda n: f"cidade_{n}")
    cep = factory.Sequence(lambda n: f"cep_{n}")
    UF = factory.Sequence(lambda n: f"UF_{n}")
    gerente = factory.Sequence(lambda n: f"gerente_{n}")
    