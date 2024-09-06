import datetime
from typing import List, Dict

from sqlalchemy import String, Integer, ARRAY, JSON, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from app.auth.database import Base


class Personal(Base):
    __tablename__ = 'personal'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(length=24), index=True)
    surname: Mapped[str] = mapped_column(String(length=24), index=True)
    fathername: Mapped[str] = mapped_column(String(length=24), index=True)
    phone_number: Mapped[str] = mapped_column(String(length=12), index=True)
    email: Mapped[str] = mapped_column(String, index=True, nullable=False)
    social_network: Mapped[List[Dict]] = mapped_column(JSON, nullable=True)
    address: Mapped[str] = mapped_column(index=True, nullable=True)
    birth_date: Mapped[str] = mapped_column(String, index=True, nullable=True)
    main_image: Mapped[str] = mapped_column(index=True, nullable=True)

    created_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True), default=lambda: datetime.datetime.now(datetime.timezone.utc))
    updated_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True), default=lambda:  datetime.datetime.now(datetime.timezone.utc),
                                                          onupdate=lambda: datetime.datetime.now(datetime.timezone.utc))
