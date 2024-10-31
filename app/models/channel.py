import datetime

from sqlalchemy import Integer, String, TIMESTAMP
from sqlalchemy.orm import mapped_column, Mapped

from app.auth.database import Base


class Channel(Base):
    __tablename__ = 'channel'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(length=36))
    url: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True),
                                                          default=lambda: datetime.datetime.now(datetime.timezone.utc))
    updated_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True),
                                                          default=lambda: datetime.datetime.now(datetime.timezone.utc),
                                                          onupdate=lambda: datetime.datetime.now(datetime.timezone.utc))
