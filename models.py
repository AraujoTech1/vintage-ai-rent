from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Carro(Base):
    __tablename__ = "carros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    ano = Column(Integer)
    cor = Column(String)
    tipo = Column(String)
    preco_dia = Column(Float)
