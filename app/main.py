from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.auth.base_config import router as auth_router
from app.auth.database import create_db_and_tables
from app.api import router


@asynccontextmanager
async def lifespan(main_app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(
    title="Personal Webpage of Batirniyaz",
    version="0.1",
    summary="This is the personal webpage of Batirniyaz, where I will post my activity.",
    lifespan=lifespan,
)

app.include_router(auth_router)
app.include_router(router)

