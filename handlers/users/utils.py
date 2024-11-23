from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Any, Callable, Type
from core import Image, User, Tweet
from .schemes import CreateUser


async def get_by_api_key(session: AsyncSession, api_key: str) -> dict | None:
    stmt = select(User.__table__._columns.name, User.__table__._columns.id).where(
        User.key == api_key
    )
    select_result = await session.execute(stmt)
    return select_result.mappings().one_or_none()
