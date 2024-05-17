from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat



class Atleta(BaseModel):
    nome: str
    cpf:str
    idade: int
    peso: PositiveFloat
    altura: PositiveFloat
    sexo: str
    categoria_id:int
    centro_treinamento_id:int
    

class Categoria(BaseModel):
    nome: str
    
class Centro_Treinamento(BaseModel):
    nome:str
    endereco:str #Esta ruim
    propietario:str