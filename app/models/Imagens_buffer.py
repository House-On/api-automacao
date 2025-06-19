
from sqlalchemy import String, Column, Integer, LargeBinary, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from ..db.database import Base

class Imagens(Base):
    __tablename__ = "imagens_buffer"

    imagens_id = Column(Integer, primary_key=True, index=True)
    dados = Column(LargeBinary, nullable=False)
    status = Column(String, default="pendente")
    upload_timestamp = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    historico_id = Column(Integer, ForeignKey("historicos.historico_id"))

    historico = relationship("Historico", back_populates="imagens")