
from fastapi import FastAPI
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from db.database import Base, engine
import os

load_dotenv()  # Carrega as variáveis do .env

# Para criar e dar drop no banco toda vez que iniciar o backend
@asynccontextmanager
async def lifespan(app: FastAPI):
    if os.getenv("ENV") == "dev":
        print("🧪 [DEV MODE] Resetando banco de dados...")
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}


