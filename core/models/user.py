"""
файл для модели user
"""
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from typing import List
from base import Base


class User(Base):
    name: Mapped[str] = mapped_column(String(100), unique=True)

    following_ids: Mapped[List[int]] = mapped_column(ForeignKey("userfallow.autor_id"))
    followers_ids: Mapped[List[int]] = mapped_column(ForeignKey("userfallow.follower_id"))
    liked_tweets: Mapped[List["Tweet"]] = relationship(back_populates="liked_users", uselist=True, secondary="userliketweet")