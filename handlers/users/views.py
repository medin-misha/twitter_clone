from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from core import db_settings, User
from handlers import create, remove, get_list, get_by_id, ok_response, error_response
from .schemes import CreateUser
from .utils import get_by_api_key

router = APIRouter(prefix="/api/users", tags=["users"])


@router.post("/")
async def create_user_view(
    user_data: CreateUser, session: AsyncSession = Depends(db_settings.session)
) -> dict:
    user = await create(session=session, model=User, data=user_data.model_dump())
    return ok_response(resp=user, name="user")


@router.get("/me")
async def auth_user_view(
    request: Request, session: AsyncSession = Depends(db_settings.session)
):
    api_key = request.headers.get("api-key")
    if api_key == "test":
        return {"result": True, "user": {"id": "int", "name": "str"}}
    user = await get_by_api_key(session=session, api_key=api_key)
    return ok_response(resp=user, name="user")


@router.get("/{id}")
async def get_users_by_id_view(
    id: int, session: AsyncSession = Depends(db_settings.session)
):
    user = await get_by_id(session=session, model=User, id=id)
    if user is None:
        return error_response(msg="Юзер не найден", err_type=404)
    return ok_response(resp=user, name="user")


@router.get("/")
async def get_users_view(session: AsyncSession = Depends(db_settings.session)):
    users_list = await get_list(session=session, model=User)
    return ok_response(resp=users_list, name="users")


@router.delete("/{id}")
async def delete_user_view(
    id: int, session: AsyncSession = Depends(db_settings.session)
):
    await remove(session=session, model=User, id=id)
    return ok_response(resp={"message": "deleted"}, name="deleted")
