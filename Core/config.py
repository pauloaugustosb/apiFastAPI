from typing import List

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://paulo:vanessa@localhost:5432/Cursos'
    DBBaseModel = declarative_base()
    
    #   Token
    JWT_SECRET: str = 'wmcYAiFL7PKDxWk_od9B7KXW2zNjB3IfvSUdM3wEQkg'
    '''''''''''''''''''''
    #   Criação do token
    import secrets
    token: str = secrets.token_urlsafe
    '''''''''''''''''''''
    ALGORITHM: str = 'HS256'  

    #   Tempo em minutos para expirar o Token  - 60min * 24h * 7dias => 1 semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24*7
    
    class Config:
        case_sensitive = True
    
settings: Settings = Settings()