from ninja import schema

class ServicoNestedInGrupoDeServicoSchema(schema.Schema):
    nome: str
    descricao: str
    metodo: str
    id: int
    
    class Config:
        orm_mode = True