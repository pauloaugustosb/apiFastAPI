from typing import AsyncGenerator, Optional

from fastapi import Depends, HTTPException, status

from jose import jwt, JWTError # type: ignore

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from pydantic import BaseModel

from Core.database import Session   
from Core.auth import oauth2_schema
from Core.config import settings
from Models.usuario_models import UsuarioModel


class TokenData(BaseModel):
    username: Optional[str] = None
    
async def get_session() -> AsyncGenerator:
    session: AsyncSession = Session()
    try:
        yield session
    finally:
        await session.close()


#   Decodificar e retonar o usuário       
async def get_current_user(db: AsyncSession = Depends(get_session), 
                           token: str = Depends(oauth2_schema)) -> UsuarioModel:
    
    #   Error
    credential_exception: HTTPException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Credenciais não autenticadas',
        headers= {'WWW-Authenticate': 'Bearer'},
    )
    
    #   Decoficação do Token
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={"verify_aud": False}
        )
        username: str = payload.get("sub")  #   Passando a chave
        
        if username is None:
            raise credential_exception
        
        token_data: TokenData = TokenData(username=username)
        
    except JWTError:
        raise credential_exception
    
    #   Pegar usuario no sistema
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == int(token_data.username))
        result = await session.execute(query)
        usuario: UsuarioModel = result.scalars().unique().one_or_none()
        
        if usuario is None:
            return credential_exception
        return usuario