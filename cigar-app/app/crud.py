from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import User, Cigar
from app.schemas import UserCreate, CigarCreate
from sqlalchemy.exc import IntegrityError
from app.auth import get_password_hash
from sqlalchemy.orm import selectinload

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalars().first()

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalar_one_or_none()

async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(select(User).filter(User.username == username))
    return result.scalars().first()


async def get_users(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(User).offset(skip).limit(limit))
    users = result.scalars().all()
    return users

async def create_user(db: AsyncSession, user: UserCreate):
    hashed_password = get_password_hash(user.password)  # Remove await
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(
        select(User).where(User.username == username)
    )
    return result.scalar_one_or_none()

async def create_cigar(db: AsyncSession, cigar: CigarCreate):
    db_cigar = Cigar(**cigar.dict())
    db.add(db_cigar)
    await db.commit()
    await db.refresh(db_cigar)
    return db_cigar


async def get_cigars(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Cigar).offset(skip).limit(limit))
    return result.scalars().all()