from ninja import schema


class LaboratorioNestedInGrupoSchema(schema.Schema):
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