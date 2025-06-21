
import os
from fastapi import FastAPI
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from app.db.database import Base, engine
from app.models.Analise import Analise
from app.models.Empresa import Empresa
from app.models.Historico import Historico
from app.models.Imagens_buffer import Imagens

from app.controllers.chatbot_controller import router as chatbot_router

# Carrega as variáveis do .env
load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    if os.getenv("ENV") == "dev":
        print("[DEV MODE] Verificando se banco precisa ser criado...")
        Base.metadata.create_all(bind=engine)
    yield

# Instancia a aplicação principal e define uma regra de criação do banco antes do início da mesma.
app = FastAPI(lifespan=lifespan)

# Inclui as rotas do chatbot controller na aplicação principal
app.include_router(chatbot_router, prefix="/chat", tags=["Chats"])

@app.get("/")
def read_root():
    return {"Hello": "World"}