from ninja import schema
from typing import List
from api.schemas.nested_schemas.servicos_nested_in_grupo_de_servico_schema import ServicoNestedInGrupoDeServicoSchema

class GrupoDeServicoNestedInLaboratorioSchema(schema.Schema):
    nome: str
    descricao: str
    status: str
    id: int
    
    servicos:List[ServicoNestedInGrupoDeServicoSchema] = []
    
    class Config:
        orm_mode = True