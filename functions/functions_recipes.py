from database.database import *
from sqlalchemy.orm import Session


def add_receita(nome,data,infos,user_name,tipo):
    with Session(engine) as session:
      new_receita = Receitas(nome=nome,data=data,infos=infos,user_name=user_name,tipo=tipo)
      session.add(new_receita)
      session.commit()
      return True if new_receita else False

def get_receita(nome):
    with Session(engine) as session:
      receita = session.query(Receitas).filter(Receitas.nome == nome).all()
      return receita
    
def exclude_receita(id):  
    with Session(engine) as session:
      receita = session.query(Receitas).filter(Receitas.id == id).first()
      session.delete(receita)
      session.commit()
      return True if receita else False 
    
def update_receita(id,infos):
    with Session(engine) as session:
      receita = session.query(Receitas).filter(Receitas.id == id).update(infos=infos)
      session.commit()
      return True if receita else False
    
def get_receitas():
    with Session(engine) as session:
      receitas = session.query(Receitas).all()
      return receitas 
