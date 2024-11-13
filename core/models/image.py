"""
файл для модели image    
"""

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from .base import Base


class Image(Base):
    filename: Mapped[str] = mapped_column(unique=True, primary_key=True)
    tweet_id: Mapped[int] = mapped_column(ForeignKey("Tweet.id"))