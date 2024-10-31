from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.channel import Channel


async def create_channel(db: AsyncSession, name: str, url: str):
    try:
        db_channel = Channel(
            name=name,
            url=url,
        )
        db.add(db_channel)
        await db.commit()
        await db.refresh(db_channel)

        return db_channel
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_channels(db: AsyncSession):
    result = await db.execute(select(Channel))
    channels = result.scalars().all()
    if not channels:
        raise HTTPException(status_code=404, detail="Channel not found")

    return channels


async def get_channel(db: AsyncSession, channel_id: int):
    db_channel = await db.execute(select(Channel).filter_by(id=channel_id))
    db_channel = db_channel.scalar_one_or_none()

    if not db_channel:
        raise HTTPException(status_code=404, detail="Channel not found")

    return db_channel


async def update_channel(db: AsyncSession, channel_id: int, name: str, url: str):
    try:
        db_channel = await get_channel(db, channel_id)

        db_channel.name = name
        db_channel.url = url

        await db.commit()

        return db_channel
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def delete_channel(db: AsyncSession, channel_id: int):
    db_channel = await get_channel(db, channel_id)
    await db.delete(db_channel)
    await db.commit()
    return HTTPException(status_code=status.HTTP_200_OK, detail="Channel deleted")

