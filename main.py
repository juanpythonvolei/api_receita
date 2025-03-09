from fastapi import FastAPI
from functions.functions_users import *
from functions.functions_recipes import *

app = FastAPI()

@app.get("/login/")
def adicionar_usuario(nome:str,usuario:str,email:str):
    try:
        add_user(nome,usuario,email)
        return {'data':'ok'}
    except:
        return {'data':'error'}

@app.get("/usuario/verificacao/")
def read_item(email:str,senha:int):
    usuario = get_user(email,senha)
    if usuario :
        return {'data':usuario}
    else:
        return {'data':'error'}
    
@app.get("/usuarios/alteracao/senha/")
def alterar_senha_usuario(id:int,senha:int):
    nova_senha = modify_user_password(id,senha)
    if nova_senha:
        return {'data':'ok'}
    else:
       return{'data':'error'}

@app.get("/usuarios/alteracao/nome/")
def alterar_nome_usuario(id:int,nome:str):
    novo_nome = modify_user_name(id,nome)
    if novo_nome:
        return {'data':'ok'}
    else:
       return{'data':'error'}
    
@app.get("/usuarios/exclusao/")
def apagar_usuario(id:int):
    if exclude_user(id):
      return {'data':'ok'}
    else:
       return {
          'data':'erro'
       }

@app.get("/receitas/")
def ver_receitas():
    receitas = get_receitas()
    return {
        'data':receitas
    }

@app.get("/receitas/exclusao/")
def excluir_receitas(id:int):
    if exclude_receita(id=id):
      return {'data':'ok'}
    else:
      return {'data':'error'}
    
@app.get("/receitas/adicao/")
def adicionar_receitas(nome:str,data:str,infos:str,user_name:str,tipo:str):
    if add_receita(nome=nome,data=data,infos=infos,user_name=user_name,tipo=tipo):
      return {'data':'ok'}
    else:
      return {'data':'error'}


@app.get("/receitas/nome/")
def ver_receitas_especificas(nome:str):
    receitas = get_receita(nome)
    return {
        'data':receitas
    }      

@app.get("/receitas/alteracao/")
def alterar_receitas(id:int,infos:str):
  if update_receita(id=id,infos=infos):
      return {'data':200}
  else:
     return {'data':'error'}





