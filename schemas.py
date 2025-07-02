from pydantic import BaseModel
from typing import Optional
from datetime import date

class LegislationBase(BaseModel):
    title: str
    type: str
    status: str
    introduced_date: Optional[date] = None
    passed_date: Optional[date] = None
    summary: Optional[str] = None
    document_url: Optional[str] = None

class LegislationCreate(LegislationBase):
    pass

class LegislationUpdate(BaseModel):
    title: Optional[str] = None
    type: Optional[str] = None
    status: Optional[str] = None
    introduced_date: Optional[date] = None
    passed_date: Optional[date] = None
    summary: Optional[str] = None
    document_url: Optional[str] = None

class Legislation(LegislationBase):
    id: int

    class Config:
        orm_mode = True
