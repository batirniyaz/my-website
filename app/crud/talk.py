from fastapi import HTTPException, status
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.schemas.talk import TalkCreate, TalkResponse, TalkUpdate
from app.models.talk import Talk


async def create_talk(db: AsyncSession, talk: TalkCreate):
    try:
        db_talk = Talk(**talk.model_dump())
        db.add(db_talk)
        await db.commit()
        await db.refresh(db_talk)

        return db_talk
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


async def get_talks(db: AsyncSession):
    result = await db.execute(select(Talk))
    talks = result.scalars().all()
    if not talks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Talk not found")

    return talks if talks else []


async def get_talk(db: AsyncSession, talk_id: int):
    db_talk = await db.execute(select(Talk).filter_by(id=talk_id))
    db_talk = db_talk.scalar_one_or_none()

    if not db_talk:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Talk not found")

    return db_talk


async def update_talk(db: AsyncSession, talk_id: int, talk: TalkUpdate):
    try:
        db_talk = await get_talk(db, talk_id)

        for key, value in talk.model_dump(exclude_unset=True).items():
            setattr(db_talk, key, value)

        await db.commit()

        return db_talk
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


async def delete_talk(db: AsyncSession, talk_id: int):
    db_talk = await get_talk(db, talk_id)

    await db.delete(db_talk)
    await db.commit()

    return HTTPException(status_code=status.HTTP_200_OK, detail="Talk deleted successfully")
