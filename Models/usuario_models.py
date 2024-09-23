from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from Core.config import settings

class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(256), nullable=True)   #   Não precisa de nome e sobrenome, apenas senha
    sobrenome = Column(String(256), nullable=True)
    email = Column(String(256), index=True, nullable=False, unique=True) #   Não pode usar o mesmo email
    senha = Column(String(256), nullable=False)
    eh_admin = Column(Boolean, default=False)
    #   Delete
    artigos = relationship(
        "ArtigoModel",
        cascade= "all, delete-orphan",
        back_populates= "criador",
        uselist= True,    #   Busca uma lista
        lazy= "joined"   #   Melhor performance
    )