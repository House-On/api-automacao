
from fastapi import FastAPI
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from app.db.database import Base, engine
import os
from app.models.Analise import Analise
from app.models.Empresa import Empresa
from app.models.Historico import Historico
from app.models.Imagens_buffer import Imagens

# Carrega as variáveis do .env
load_dotenv()

# Para criar e dar drop no banco toda vez que iniciar o backend
@asynccontextmanager
async def lifespan(app: FastAPI):
    if os.getenv("ENV") == "dev":
        print("[DEV MODE] Resetando banco de dados...")
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

# Requisição raiz do main
@app.get("/")
def read_root():
    return {"Hello": "World"}


