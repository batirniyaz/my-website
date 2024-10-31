from pydantic import BaseModel, Field
import datetime


class ChannelResponse(BaseModel):
    id: int = Field(..., description="The ID of the channel")
    name: str = Field(..., min_length=3, max_length=36, description="The name of the channel", examples=["First channel"])
    url: str = Field(..., description="The url of the channel", examples=["https://www.youtube.com/channel/1234567890"])
    created_at: datetime.datetime = Field(..., description="The time the channel was created")
    updated_at: datetime.datetime = Field(..., description="The time the channel was updated")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Telegram",
                "url": "https://t.me/batirniyaz",
                "created_at": "2021-08-01T12:00:00",
                "updated_at": "2021-08-01T12:00:00"
            }
        }