from fastapi import APIRouter
from .personal import router as personal_router
from .talk import router as talk_router
from .channel import router as channel_router

router = APIRouter()

router.include_router(personal_router, prefix="/personal", tags=["Personal"])
router.include_router(talk_router, prefix="/talk", tags=["Talk"])
router.include_router(channel_router, prefix="/channel", tags=["Channel"])
