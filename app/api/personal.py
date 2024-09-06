from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.database import get_async_session
from app.crud.personal import (
    create_personal,
    upload_main_image,
    get_personals,
    update_personal,
    delete_personal
)
from app.schemas.personal import PersonalCreate, PersonalResponse, PersonalUpdate

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


@router.post("/upl_img", response_model=PersonalResponse)
async def upload_main_image_endpoint(
        person_id: int,
        file: UploadFile = File(),
        db: AsyncSession = Depends(get_async_session)
):
    """
    Upload main image
    """
    return await upload_main_image(db, file, person_id)


@router.get("/", response_model=List[PersonalResponse])
async def get_personals_endpoint(
        db: AsyncSession = Depends(get_async_session)
):
    """
    Get a list of personals
    """
    return await get_personals(db)


@router.put("/{person_id}", response_model=PersonalResponse)
async def update_personal_endpoint(
        person_id: int,
        personal: PersonalUpdate,
        db: AsyncSession = Depends(get_async_session)
):
    """
    Update personal
    """
    return await update_personal(db, person_id, personal)


@router.delete("/{person_id}")
async def delete_personal_endpoint(
        person_id: int,
        db: AsyncSession = Depends(get_async_session)
):
    """
    Delete personal
    """
    return await delete_personal(db, person_id)
