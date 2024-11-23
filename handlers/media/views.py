from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, UploadFile, Request, Form
from annotated_types import Annotated
from typing import Dict
from handlers import (
    ok_response,
    error_response,
    create,
    get_by_id,
    remove,
    get_user_by_api_key,
)
from core import Image, db_settings
from .utils import save_image


router = APIRouter(prefix="/api/medias", tags=["medias"])


@router.post("")
async def create_image_view(
    request: Request,
    file: Annotated[UploadFile, Form()],
    session: AsyncSession = Depends(db_settings.session),
) -> Dict[str, bool | int]:
    user = await get_user_by_api_key(
        session=session, api_key=request.headers.get("api-key")
    )
    if user is None:
        return error_response(msg="неправильный api key", err_type=405)
    id = await save_image(file=file, session=session)
    return ok_response(resp=id, name="media_id")
