from fastapi import FastAPI
from app.routers import auth, cigars, users
from app.database import engine, Base

import asyncio

app = FastAPI()


# Include routers
app.include_router(auth.router)
app.include_router(cigars.router)
app.include_router(users.router)



@app.get("/")
def read_root():
    return {"message": "Welcome to the Cigar Collection Management API"}

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()
