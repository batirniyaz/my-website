from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.database import get_async_session
from app.crud.channel import create_channel, get_channels, get_channel, update_channel, delete_channel
from app.schemas.channel import ChannelResponse

router = APIRouter()


@router.post("/", response_model=ChannelResponse)
async def create_channel_endpoint(
        name: str = Query(..., min_length=1, max_length=100, regex=r"^[A-Za-z0-9 ]+$", example="Back of Batya"),
        url: str = Query(..., min_length=1, example="https://t.me/backbatya"),
        db: AsyncSession = Depends(get_async_session),
):
    """
    Create a new channel with the given details.
    """
    return await create_channel(db, name, url)


@router.get("/", response_model=List[ChannelResponse])
async def get_channels_endpoint(
        db: AsyncSession = Depends(get_async_session)
):
    """
    Get a list of channels
    """
    return await get_channels(db)


@router.get("/{channel_id}", response_model=ChannelResponse)
async def get_channel_endpoint(
        channel_id: int,
        db: AsyncSession = Depends(get_async_session)
):
    """
    Get a channel by id
    """
    return await get_channel(db, channel_id)


@router.put("/{channel_id}", response_model=ChannelResponse)
async def update_channel_endpoint(
        channel_id: int,
        name: str = Query(..., min_length=1, max_length=100, regex=r"^[A-Za-z0-9 ]+$", example="Back of Batya"),
        url: str = Query(..., min_length=1, example="https://t.me/backbatya"),
        db: AsyncSession = Depends(get_async_session)
):
    """
    Update a channel by id
    """
    return await update_channel(db, channel_id, name, url)


@router.delete("/{channel_id}")
async def delete_channel_endpoint(
        channel_id: int,
        db: AsyncSession = Depends(get_async_session)
):
    """
    Delete a channel by id
    """
    return await delete_channel(db, channel_id)