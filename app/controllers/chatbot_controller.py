
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schema.chat_schema import ChatSchema
from app.db.database import get_db
from app.models.Empresa import Empresa
from app.services.groq_service import enviar_para_groq
from app.utils.modelo_resposta import resposta_api

router = APIRouter()

@router.post("/")
def enviar_mensagem_ia(chat: ChatSchema, db: Session = Depends(get_db)):

    '''Método responsável pelo recebimento da requisição do usuário pelo frontend

    Args:
        chat (ChatSchema): Representa os dados recebidos a partir da requisição, sendo eles o id da empresa e a mensagem de pergunta do usuário.
        db (Session): Representa a sessão para acessar o banco de dados.

    Raises:
        HTTPException: Caso a empresa que enviou a mensagem não exista no banco.

    Returns:
        resposta_api: O modelo padrão de resposta do backend, com a resposta da IA e o sucesso na comunicação, além do status http.
    
    '''

    empresa = db.query(Empresa).filter(Empresa.empresa_id == chat.empresa_id).first()

    print(empresa.nome)

    if not empresa:
        raise HTTPException(status_code=404, detail="Essa empresa não existe.")
    
    mensagem_usuario = chat.mensagem
    descricao_empresa = empresa.descricao_geral
    nome_empresa = empresa.nome

    resposta = enviar_para_groq(mensagem=mensagem_usuario, descricao=descricao_empresa, nome=nome_empresa)

    return resposta_api(
        mensagem_sistema="Resposta enviada com Sucesso.",
        dados=resposta,
        status_code=200
    )


