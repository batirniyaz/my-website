from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.auth.base_config import router as auth_router
from app.auth.database import create_db_and_tables


@asynccontextmanager
async def lifespan(main_app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)

