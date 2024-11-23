from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import Result, select
from fastapi import UploadFile, Form
import httpx
from typing import Annotated
from core import Image, config
from handlers import create, remove


async def save_image(file: Annotated[UploadFile, Form()], session: AsyncSession) -> int:

    async with httpx.AsyncClient() as client:
        response = await client.post(
            config.image_saver_url + "image/",
            files={"image": (file.filename, await file.read(), file.content_type)},
        )
    filename = response.text.replace('"', "")

    stmt = insert(Image.__table__).values(filename=filename)
    await session.execute(stmt)
    await session.commit()

    select_stmt = select(Image.__table__._columns.id).where(Image.filename == filename)
    select_result: Result = await session.execute(select_stmt)
    return select_result.scalar()


async def get_image(filename: str):
    print(123123)
    async with httpx.AsyncClient() as client:
        response = await client.get(config.image_saver_url + "images/" + filename)
    return response.content
