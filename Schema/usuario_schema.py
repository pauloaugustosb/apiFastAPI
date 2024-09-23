from typing import Optional
from typing import List

from pydantic import BaseModel, EmailStr

from Schema.artigo_schema import ArtigoSchema


#   Dados básicos do usuário
class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False
    
    class Config:
        orm_mode = True
 
#   Herda a classe de usuario, possibilita devolver as informações sem enviar a senha       
class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str
    

#   Lista artigos relacionados com o usuario    
class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: Optional[List[ArtigoSchema]]
   

#   Atualização dos dados do usuário    
class UsuarioSchemaUp(UsuarioSchemaBase):
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    eh_admin: Optional[bool]