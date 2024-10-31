import datetime

from pydantic import BaseModel, Field
from typing import Optional


class TalkBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=36, description="The title of the talk", examples=["First talk"])
    video_url: str = Field(..., description="The video url of the talk", examples=["https://www.youtube.com/watch?v=1234567890"])


class TalkCreate(TalkBase):
    pass


class TalkUpdate(TalkBase):
    title: Optional[str] = Field(None, min_length=3, max_length=36, description="The title of the talk", examples=["First talk"])
    video_url: Optional[str] = Field(None, description="The video url of the talk", examples=["https://www.youtube.com/watch?v=1234567890"])


class TalkResponse(TalkBase):
    id: int = Field(..., description="The ID of the talk")
    created_at: datetime.datetime = Field(..., description="The time the talk was created")
    updated_at: datetime.datetime = Field(..., description="The time the talk was updated")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "First talk",
                "video_url": "https://www.youtube.com/watch?v=1234567890",
                "created_at": "2021-08-01T12:00:00",
                "updated_at": "2021-08-01T12:00:00"
            }
        }
