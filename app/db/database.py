
from os import makedirs
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

caminho_banco = "./app/data"
makedirs(caminho_banco, exist_ok=True)

DATABASE_URL = f"sqlite:///{caminho_banco}/banco.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    '''Método responsável por iniciar uma sessão no banco de dados.'''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()