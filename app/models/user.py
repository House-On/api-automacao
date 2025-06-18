
from sqlalchemy import Column, String, Integer

from ..db.database import Base

class User(Base):
    __tablename__ = "usuarios"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    CNPJ = Column(String(50), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    general_description = Column(String(150), nullable=False)
    summary = Column(String(255))