from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Query
from fastapi_cache.decorator import cache
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.database import get_async_session
from app.crud.talk import create_talk, get_talks, get_talk, update_talk, delete_talk
from app.schemas.talk import TalkCreate, TalkResponse, TalkUpdate

router = APIRouter()


@router.post("/", response_model=TalkResponse)
async def create_talk_endpoint(
        talk: TalkCreate,
        db: AsyncSession = Depends(get_async_session),
):
    """
    Create a new talk with the given details.
    """
    return await create_talk(db, talk)


@router.get("/", response_model=List[TalkResponse])
@cache(expire=60)
async def get_talks_endpoint(
        db: AsyncSession = Depends(get_async_session)
):
    """
    Get a list of talks
    """
    return await get_talks(db)


@router.get("/{talk_id}", response_model=TalkResponse)
@cache(expire=60)
async def get_talk_endpoint(
        talk_id: int,
        db: AsyncSession = Depends(get_async_session)
):
    """
    Get a talk by id
    """
    return await get_talk(db, talk_id)


@router.put("/{talk_id}", response_model=TalkResponse)
async def update_talk_endpoint(
        talk_id: int,
        talk: TalkUpdate,
        db: AsyncSession = Depends(get_async_session)
):
    """
    Update a talk by id
    """
    return await update_talk(db, talk_id, talk)


@router.delete("/{talk_id}")
async def delete_talk_endpoint(
        talk_id: int,
        db: AsyncSession = Depends(get_async_session)
):
    """
    Delete a talk by id
    """
    return await delete_talk(db, talk_id)
