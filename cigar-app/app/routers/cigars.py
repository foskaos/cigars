from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas import Cigar, CigarCreate
from app.crud import get_cigars, create_cigar
from app.dependencies import get_db

router = APIRouter(prefix="/cigars", tags=["cigars"])

@router.get("/", response_model=List[Cigar])
def read_cigars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cigars = get_cigars(db, skip=skip, limit=limit)
    return cigars

@router.post("/", response_model=Cigar)
def add_cigar(cigar: CigarCreate, db: Session = Depends(get_db)):
    return create_cigar(db=db, cigar=cigar, user_id=1)  # Placeholder for user_id
