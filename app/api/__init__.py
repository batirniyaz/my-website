from fastapi import APIRouter
from .personal import router as personal_router

router = APIRouter()

router.include_router(personal_router, prefix="/personal", tags=["Personal"])
