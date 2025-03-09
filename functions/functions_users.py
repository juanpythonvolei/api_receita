from database.database import *
from sqlalchemy.orm import Session

def add_user(nome,usuario,email):
    with Session(engine) as session:
      new_user = Usuario(nome=nome,usuario=usuario,email=email)
      session.add(new_user)
      session.commit()
      return True if new_user else False
    
def get_user(email:str,senha:int):
    with Session(engine) as session:
      user = session.query(Usuario).filter(Usuario.email == email,Usuario.senha == senha).first()
      if user == None:
        return False
      return user
    
def exclude_user(id):
    with Session(engine) as session:
      user = session.query(Usuario).filter(Usuario.id == id).first()
      session.delete(user)
      session.commit()
      return True if user else False
    
def modify_user_password(id,nova_senha):
   with Session(engine) as session:
      user = session.query(Usuario).filter(Usuario.id == id).update(senha = nova_senha)
      session.commit()
      return True if user else False
    
def modify_user_name(id,novo_nome):
   with Session(engine) as session:
      user = session.query(Usuario).filter(Usuario.id == id).update(nome = novo_nome)
      session.commit()
      return True if user else False