from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.schemas import Cigar, CigarCreate, User
from app.crud import get_cigars, create_cigar
from app.dependencies import get_db
from app.auth import get_current_user

router = APIRouter(prefix="/cigars", tags=["cigars"])

@router.get("/", response_model=List[Cigar])
async def read_cigars(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    cigars = await get_cigars(db, skip=skip, limit=limit)  # Ensure this function is awaited
    return cigars

@router.post("/", response_model=Cigar)
async def add_cigar(cigar: CigarCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await create_cigar(db=db, cigar=cigar)  # Ensure this function is awaited
