from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import asynccontextmanager

DATABASE_URL = "postgresql+asyncpg://user:password@db/cigar_db"

# Create an asynchronous engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create an asynchronous sessionmaker
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Create a base class for the models
Base = declarative_base()

@asynccontextmanager
async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
