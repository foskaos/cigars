from pydantic import BaseModel
from typing import List, Optional


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
class CigarBase(BaseModel):
    name: str
    brand: str
    origin: Optional[str] = None
    ring_gauge: Optional[int] = None
    length: Optional[int] = None

class CigarCreate(CigarBase):
    pass

class Cigar(CigarBase):
    id: int
    # owner_id: int

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