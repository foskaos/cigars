from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.schemas import User, UserCreate
from app.crud import get_users, create_user
from app.dependencies import get_db
from app.auth import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    users = await get_users(db, skip=skip, limit=limit)
    return users

@router.post("/", response_model=User)
async def add_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db=db, user=user)
