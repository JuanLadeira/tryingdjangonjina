from ninja import Schema
from typing import List
from api.schemas.nested_schemas.grupo_de_servico_nested_in_laboratorio_schema import GrupoDeServicoNestedInLaboratorioSchema


class LaboratorioCreateUpdateSchema(Schema):
    nome: str
    id: int
    endereco: str
    status: str
    numero_da_acreditacao: str
    situacao: str
    bairro: str
    cidade: str
    cep: str
    telefone: str
    UF: str
    gerente: str
    email: str
    
    class Config:
        orm_mode = True


class LaboratorioReadSchema(Schema):
    nome: str
    id: int
    endereco: str
    status: str
    numero_da_acreditacao: str
    situacao: str
    bairro: str
    cidade: str
    cep: str
    telefone: str
    UF: str
    gerente: str
    email: str
    grupos_de_servico: List[GrupoDeServicoNestedInLaboratorioSchema] = []

    class Config:
        orm_mode = True
