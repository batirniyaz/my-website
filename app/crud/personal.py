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


async def upload_main_image(db: AsyncSession, file: UploadFile, person_id: int):
    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION_NAME
        )

        s3.upload_fileobj(
            file.file,
            AWS_BUCKET_NAME,
            file.filename,
            ExtraArgs={"ContentType": file.content_type}
        )

        image_url = f"https://{AWS_BUCKET_NAME}.s3.{AWS_REGION_NAME}.amazonaws.com/{file.filename}"

        db_personal = await db.execute(select(Personal).filter_by(id=person_id))
        db_personal = db_personal.scalar_one_or_none()

        db_personal.main_image = image_url
        await db.commit()

        return db_personal
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def get_personals(db: AsyncSession):
    result = await db.execute(select(Personal))
    personals = result.scalars().all()
    if not personals:
        raise HTTPException(status_code=404, detail="Personal not found")

    return personals
