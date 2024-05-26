from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import User, Cigar
from app.schemas import UserCreate, CigarCreate
from sqlalchemy.exc import IntegrityError

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalars().first()

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalars().first()

async def create_user(db: AsyncSession, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(username=user.username, email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    try:
        await db.commit()
        await db.refresh(db_user)
        return db_user
    except IntegrityError:
        await db.rollback()
        raise

async def get_cigars(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Cigar).offset(skip).limit(limit))
    return result.scalars().all()

async def create_cigar(db: AsyncSession, cigar: CigarCreate, user_id: int):
    db_cigar = Cigar(**cigar.dict(), owner_id=user_id)
    db.add(db_cigar)
    await db.commit()
    await db.refresh(db_cigar)
    return db_cigar
