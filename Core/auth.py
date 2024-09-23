from pytz import timezone

from typing import Optional, List
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from jose import jwt # type: ignore

from Models.usuario_models import UsuarioModel
from Core.config import settings
from Core.security import verificar_senha

from pydantic import EmailStr

#   Endpoint para autenticação com token de acesso
oauth2_schema = OAuth2PasswordBearer(
    tokenUrl= f"{settings.API_V1_STR}/usuarios/login"
)

async def autenticar(email: EmailStr, senha:str, db: AsyncSession) -> Optional[UsuarioModel]:
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.email == email)
        result = await session.execute(query)
        usuario: UsuarioModel = result.scalars().unique().one_or_none()
        
        if not usuario:
            return None
        if not verificar_senha(senha, usuario.senha):
            return None
        return usuario

#   Criar Token
def _criar_token(tipo_token: str, tempo_vida: timedelta, sub: str) -> str:
    #   http://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3
    payload = {}
    sp = timezone('America/Sao_Paulo')
    expira = datetime.now(tz=sp) + tempo_vida
    
    payload["type"] = tipo_token
    
    payload["exp"] = expira
    
    payload["iat"] = datetime.now(tz=sp)
    
    payload["sub"] = str(sub)
    
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)

def criar_token_acess(sub:str) -> str:
    #   https://jwt.io
    return _criar_token(
        tipo_token='access_token',
        tempo_vida=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub
    )