from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Author(Base):
    """
    Автор sqlalchemy-модель
    """

    __tablename__ = 'authors'

    # полное имя
    full_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    # год рождения
    birth_year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    # описание (если есть)
    bio: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # время создания
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # время обновления
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
