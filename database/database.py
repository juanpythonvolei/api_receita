from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
import os

Base = declarative_base()
DATABASE_URL = f"{os.getenv('DATABASE_URL')}"  
# Substitua pelos detalhes do seu banco

# Criar engine de conexão
engine = create_engine(DATABASE_URL, echo=True)  # echo=True mostra logs das operações

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True,unique=True)
    nome = Column(String, nullable=False)
    usuario = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(Integer)
class Receitas(Base):
    __tablename__ = 'receitas'
    id = Column(Integer, primary_key=True, autoincrement=True,unique=True)
    nome = Column(String, nullable=False)
    data = Column(String, nullable=False)
    infos = Column(String, nullable=False)
    user_name = Column(String)
    tipo = Column(String, nullable=False)

Base.metadata.create_all(engine)
