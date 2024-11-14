from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Callable, Type
from core import Image, User, Tweet
from .schemes import CreateUser


async def create_user(
    session: AsyncSession,
    user: CreateUser,
) -> Callable:
    """
    функция которая должна создавать запись в таблице user
    """
    creating_object = User(**user.model_dump())
    async with session.begin():
        session.add(creating_object)
        await session.commit()
    await session.refresh(creating_object)
    return creating_object