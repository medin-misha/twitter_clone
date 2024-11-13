"""
файл для модели tweet
"""
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List
from .base import Base


class Tweet(Base):
    content: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))

    liked_users: Mapped[List["User"]] = relationship(back_populates="liked_tweets", uselist=True, secondary="userliketweet")
    autor: Mapped["User"] = relationship(back_populates="tweets", uselist=False)
    attachments: Mapped[List["Image"]] = relationship(uselist=True)
