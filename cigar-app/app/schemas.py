from pydantic import BaseModel
from typing import List, Optional

class CigarBase(BaseModel):
    name: str
    brand: str
    origin: str
    flavor_notes: Optional[str] = None
    rating: Optional[int] = None

class CigarCreate(CigarBase):
    pass

class Cigar(CigarBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    cigars: List[Cigar] = []

    class Config:
        orm_mode = True
