from ninja import Schema
from typing import List, Optional

from api.schemas.nested_schemas.laboratorio_nested_in_grupo_schema import LaboratorioNestedInGrupoSchema
from api.schemas.nested_schemas.servicos_nested_in_grupo_de_servico_schema import ServicoNestedInGrupoDeServicoSchema



class GrupoDeServicoCreateUpdateSchema(Schema):
    nome: str
    id: int
    laboratorio: int
   
    
    class Config:
        orm_mode = True


class GrupoDeServicoReadSchema(Schema):
    nome: str
    id: int
    laboratorio: LaboratorioNestedInGrupoSchema
    servicos: List[ServicoNestedInGrupoDeServicoSchema] = []
    
    class Config:
        orm_mode = True