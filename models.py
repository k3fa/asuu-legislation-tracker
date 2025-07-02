from sqlalchemy import Column, Integer, String, Text, Date
from .database import Base

class Legislation(Base):
    __tablename__ = "legislation"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    type = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)
    introduced_date = Column(Date)
    passed_date = Column(Date)
    summary = Column(Text)
    document_url = Column(Text)
