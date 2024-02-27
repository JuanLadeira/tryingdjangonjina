from ninja import Schema

class ServicoSchemaCreateUpdateRead(Schema):
    nome: str
    descricao: str
    metodo: str
    id: int
    grupo_de_servico: int
    
    class Config:
        orm_mode = True



