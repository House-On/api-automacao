
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..db.database import Base
from datetime import datetime, timezone

'''
    Classe responsável por representar o histórico de chat do usuário.
    Se relacionada com as tabelas do banco de dados: "analises" e "imagens_buffer".
    Serve como um centro de controle sobre essas tabelas.
'''

class Historico(Base):
    __tablename__ = "historicos"

    historico_id = Column(Integer, primary_key=True, index=True)
    data_inicial = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    empresa_id = Column(Integer, ForeignKey("empresas.empresa_id"), unique=True)

    # Facilita a coleta de informações, tornando os dados "bidirecionais"
    empresa = relationship("Empresa", back_populates="historico")

    analises = relationship("Analise", back_populates="historico", cascade="all, delete-orphan")
    imagens = relationship("Imagens", back_populates="historico", cascade="all, delete-orphan")

