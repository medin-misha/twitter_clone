from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core import db_settings, User
from handlers import create, delete, ok_response, error_response
from .schemes import CreateUser
from .utils import create_user

router = APIRouter(prefix="/api/users", tags=["users"])


@router.post("/")
async def create_user_view(
    user_data: CreateUser, session: AsyncSession = Depends(db_settings.session)
) -> dict:
    """
    функция которая должна создавать user
    """
    # user = await create_user(session=session, user=user_data)
    user = await create(session=session, model=User, data=user_data.model_dump())
    return f"{user}"
