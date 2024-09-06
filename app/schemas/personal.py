from fastapi import UploadFile
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
import datetime


class PersonalBase(BaseModel):
    name: str = Field(..., description="The name of the personal user")
    surname: str = Field(..., description="The surname of the personal user")
    fathername: str = Field(..., description="The fathername of the personal user")
    email: EmailStr = Field(..., description="The email of the personal user")
    phone_number: str = Field(..., description="The phone number of the personal user")
    address: Optional[str] = Field(..., description="The address of the personal user")
    birth_date: Optional[str] = Field(..., description="The birth date of the personal user")
    social_network: Optional[list] = Field([], description="The social network of the personal user")


class PersonalCreate(PersonalBase):
    pass


class PersonalUpdate(PersonalBase):
    name: Optional[str] = Field(None, description="The name of the personal user")
    surname: Optional[str] = Field(None, description="The surname of the personal user")
    fathername: Optional[str] = Field(None, description="The fathername of the personal user")
    email: Optional[EmailStr] = Field(None, description="The email of the personal user")
    phone_number: Optional[str] = Field(None, description="The phone number of the personal user")
    address: Optional[str] = Field(None, description="The address of the personal user")
    birth_date: Optional[str] = Field(None, description="The birth date of the personal user")
    social_network: Optional[list] = Field(None, description="The social network of the personal user")


class PersonalResponse(PersonalBase):
    id: int = Field(..., description="The ID of the personal user")
    main_image: Optional[str] = Field(None, description="The main image of the personal user")

    created_at: datetime.datetime = Field(..., description="The time the personal user was created")
    updated_at: datetime.datetime = Field(..., description="The time the personal user was updated")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Batirniyaz",
                "surname": "Muratbaev",
                "fathername": "Temirbek uli",
                "email": "muratbaevbatirniyaz@gmail.com",
                "phone_number": "998905913873",
                "address": "Nukus, Uzbekistan",
                "birth_date": "2005-06-14",
                "social_network": [{"telegram": "https://t.me/batirniyaz", "github": "https://github.com/batirniyaz"}],
                "main_image": "https://example.com/image.jpg",
                "created_at": "2021-08-01T12:00:00",
                "updated_at": "2021-08-01T12:00:00"
            }
        }
