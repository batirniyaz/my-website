from typing import List

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String, ARRAY, JSON, TIMESTAMP
from app.auth.database import Base
import datetime


class Blog(Base):
    __tablename__ = 'blog'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(length=36))
    content: Mapped[str] = mapped_column(String, index=True)
    tags: Mapped[List[str]] = mapped_column(ARRAY(String), nullable=True)
