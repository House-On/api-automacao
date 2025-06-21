
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.db.database import Base

'''
    Classe responsável por representar a entidade de Empresa no banco de dados.
    Cria uma tabela no banco chamada "empresas", mantém a lógica de usuário do sistema.
'''

class Empresa(Base):
    __tablename__ = "empresas"

    empresa_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    cnpj = Column(String(50), unique=True, nullable=False)
    senha = Column(String(120), nullable=False)
    descricao_geral = Column(String(150), nullable=False)
    resumo_ia = Column(String(255))

    historico = relationship("Historico", back_populates="empresa", uselist=False, cascade="all, delete-orphan")