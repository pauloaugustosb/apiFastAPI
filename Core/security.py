from passlib.context import CryptContext # type: ignore

CRIPTO = CryptContext(schemes=['bcrypt'], deprecated= 'auto')

def verificar_senha(senha: str, hash_senha: str) -> bool:
    '''''''''''''''''''''''''''
    Função que verifica se a senha está correta, comparando a senha em texto,
    informada pelo usuario, e o hash da senha que estará salvo no DB durante 
    a criação da conta
    '''''''''''''''''''''''''''
    return CRIPTO.verify(senha, hash_senha)


def gerar_hash_senha(senha: str) -> str:
    '''''''''''''''''''''''''''
    Função que retorna o hash da senha
    '''''''''''''''''''''''''''
    return CRIPTO.hash(senha)