from pydantic import BaseModel

class Resposta(BaseModel):
    nome: str
    cluster: int
    resposta: str