from sqlalchemy.ext.asyncio import AsyncSession
from typing import Callable
from core import Image, User, Tweet


async def create(
    session: AsyncSession,
    model: Image | User | Tweet,
    data: dict,
) -> Callable:
    print(model.__table__)
    creating_object = model(
        **data
    )
    async with session.begin():
        session.add(creating_object)
        await session.commit()
    await session.refresh(creating_object)
    return creating_object


async def delete(
    session: AsyncSession,
    model: Image | User | Tweet,
    id: int,
) -> bool:
    deleting_object = await session.get(model, id)
    if deleting_object is None:
        return False

    async with session.begin():
        await session.delete(deleting_object)
        await session.commit()
    return True
