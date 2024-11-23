"""
файл для модели user
"""

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from typing import List
from .base import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    key: Mapped[str] = mapped_column(unique=True)
    tweets: Mapped[List["Tweet"]] = relationship(
        back_populates="autor", lazy="selectin", uselist=True
    )


#     name: Mapped[str] = mapped_column(String(100))
#     key: Mapped[str] = mapped_column(unique=True)
#
#     following_ids: Mapped[List[int]] = relationship(
#         back_populates="autor_id",
#         secondary="userfollow",
#         secondaryjoin="user.id == userfollow.autor_id",
#     )
#     followers_id: Mapped[List[int]] = relationship(
#         back_populates="autor_id",
#         secondary="userfollow",
#         secondaryjoin="user.id == userfollow.follower_id",
#     )
#
#     liked_tweets: Mapped[List["Tweet"]] = relationship(
#         back_populates="liked_users", uselist=True, secondary="userliketweet"
#     )
