
from sqlalchemy.orm import Mapped, mapped_column, relationship 
from sqlalchemy import DateTime, ForeignKey, Integer, String, Float , Column
from datetime import datetime
from pydantic import PositiveFloat
from conexaodb import Base
from workout_api.contrib.models import Basemodel




class AtletaModel(Basemodel):
    """Declarative base model"""
    __tablename__ = 'atletas'
    pk_id :Mapped[int ]= mapped_column(Integer,primary_key=True,index=True,autoincrement=True)
    nome:Mapped[str] = mapped_column(String(40))
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[float] = mapped_column(Float, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
   
    
    
    categoria: Mapped['CategoriaModel'] = relationship('CategoriaModel', back_populates='atleta')
    categoria_id: Mapped[id] = mapped_column(ForeignKey('categorias.pk_id'),nullable=True)
    centro_treinamento: Mapped['CT_Model'] = relationship('CT_Model', back_populates='atleta')
    centro_treinamento_id: Mapped[id] = mapped_column(ForeignKey('centro_treinamento.pk_id'),nullable=True)
    
    
class CT_Model(Basemodel):
    '''Declarative model '''
    __tablename__ = 'centro_treinamento'
    pk_id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    nome:Mapped[str] = mapped_column(String(20),unique=True,nullable=False)
    endereco:Mapped[str] = mapped_column(String(60),nullable=False)
    propietario:Mapped[str] = mapped_column(String(30),nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='centro_treinamento')
    
class CategoriaModel(Basemodel):
    '''Declarative model'''
    __tablename__ = 'categorias'
    pk_id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    nome:Mapped[str] = mapped_column(String(10),unique=True,nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='categoria')
