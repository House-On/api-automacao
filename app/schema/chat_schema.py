
from pydantic import BaseModel

class ChatSchema(BaseModel):
    '''
    Chat Schema
    Responsável por representar as requisições do usuário vindas do frontend

    Args:
        BaseModel: Facilitar as validações dos campos do schema.

    Attributes:
        empresa_id: representa o id da empresa registrado no banco de dados.
        mensagem: representa a mensagem de pergunta do usuário.
    
    '''

    empresa_id: int
    mensagem: str