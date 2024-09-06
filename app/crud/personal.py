from fastapi import HTTPException, status, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import boto3

from app.schemas.personal import PersonalCreate, PersonalUpdate, PersonalResponse
from app.models.personal import Personal

from app.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION_NAME, AWS_BUCKET_NAME


async def create_personal(db: AsyncSession, personal: PersonalCreate):
    try:
        db_personal = Personal(**personal.model_dump())
        db.add(db_personal)
        await db.commit()
        await db.refresh(db_personal)

        return db_personal
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



