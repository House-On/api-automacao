
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from ..db.database import Base

class Analise(Base):
    __tablename__ = "analises"

    analise_id = Column(Integer, primary_key=True, index=True)
    mensagem_gerada = Column(String, nullable=False)
    timestamp = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    historico_id = Column(Integer, ForeignKey("historicos.historico_id"))

    historico = relationship("Historico", back_populates="analises")