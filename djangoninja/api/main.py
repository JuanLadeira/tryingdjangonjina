from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

api = NinjaAPI()

from api.models.laboratorio_model import Laboratorio


@api.get("/laboratorio")
def listar_laboratorio(request):
    laboratorios = Laboratorio.objects.all()
    response = [
        {
            "nome": l.nome, 
            "id": l.id, 
            "endereco":l.endereco, 
            "status":l.status, 
            "numero_da_acreditacao":l.numero_da_acreditacao, 
            "situacao":l.situacao, 
            "bairro":l.bairro, 
            "cidade":l.cidade, 
            "cep":l.cep, 
            "telefone":l.telefone, 
            "UF":l.UF, 
            "gerente":l.gerente, 
            "email":l.email
        } 
            for l in laboratorios
    ]
    return response


@api.get("/laboratorio/{id}")
def get_laboratorio(request, id: int):
    laboratorio = get_object_or_404(Laboratorio, id=id)
    return model_to_dict(laboratorio)