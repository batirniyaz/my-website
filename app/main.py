from contextlib import asynccontextmanager

from fastapi import FastAPI

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis

from app.auth.base_config import router as auth_router
from app.auth.database import create_db_and_tables
from app.api import router


@asynccontextmanager
async def lifespan(main_app: FastAPI):
    await create_db_and_tables()

    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="personal-website-cache")

    yield

app = FastAPI(
    title="Personal Webpage of Batirniyaz",
    version="0.1",
    summary="This is the personal webpage of Batirniyaz, where I will post my activity.",
    lifespan=lifespan,
)

app.include_router(auth_router)
app.include_router(router)

