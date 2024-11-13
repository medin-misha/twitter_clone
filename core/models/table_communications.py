"""
файл для связей между таблицами
"""

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base


class UserLikeTweet(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    tweet_id: Mapped[int] = mapped_column(ForeignKey("tweet.id"))


class UserFallow(Base):
    follower_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    autor_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
