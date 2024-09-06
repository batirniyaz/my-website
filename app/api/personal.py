from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.database import get_async_session
from app.crud.personal import create_personal, upload_main_image, get_personals
from app.schemas.personal import PersonalCreate, PersonalResponse

router = APIRouter()


@router.post("/", response_model=PersonalResponse)
async def create_personal_endpoint(
        personal: PersonalCreate,
        db: AsyncSession = Depends(get_async_session),
):
    """
    Create a new personal with the given details.
    """
    return await create_personal(db, personal)



