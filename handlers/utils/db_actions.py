from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result, delete
from sqlalchemy.dialects.postgresql import insert
from typing import Callable, List, Any
from core import Image, User, Tweet


async def create(
    session: AsyncSession,
    model: Image | User | Tweet,
    data: dict,
) -> dict[Any]:
    stmt = insert(model.__table__).values(name=data.get("name"), key=data.get("key"))
    async with session.begin():
        await session.execute(stmt)
        await session.commit()
    select_stmt = select(model.__table__).where(model.key == data.get("key"))
    select_result: Result = await session.execute(select_stmt)
    return dict(select_result.mappings().one())


async def get_by_id(
    session: AsyncSession, model: Image | User | Tweet, id: int
) -> dict | None:
    stmt = select(model.__table__._columns).where(model.id == id)
    select_result: Result = await session.execute(stmt)
    return select_result.mappings().one_or_none()


async def get_list(session: AsyncSession, model: Image | User | Tweet) -> List[dict]:
    stmt = select(model.__table__).order_by(model.name)
    select_result: Result = await session.execute(stmt)
    return select_result.mappings().all()


async def remove(
    session: AsyncSession,
    model: Image | User | Tweet,
    id: int,
) -> None:
    stmt = delete(model.__table__).where(model.id == id)

    async with session.begin():
        await session.execute(stmt)
        await session.commit()
