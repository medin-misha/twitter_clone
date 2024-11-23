"""
файл для связей между таблицами
"""

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base


class UserLikeTweet(Base):
    __tablename__ = "usersliketweets"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    tweet_id: Mapped[int] = mapped_column(ForeignKey("tweets.id"))


#     user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
#     tweet_id: Mapped[int] = mapped_column(ForeignKey("tweet.id"))
#
#
class UserFallow(Base):
    __tablename__ = "usersfallows"
    id: Mapped[int] = mapped_column(primary_key=True)
    follower_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    autor_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


#     follower_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
#     autor_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
