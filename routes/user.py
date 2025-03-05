from fastapi import APIRouter, HTTPException, status, Request
from sqlalchemy import select

from database import SessionDB, UserModel
from schemas.users import UserDataSchema


router = APIRouter(prefix='/user', tags=['User'])


@router.get(path='/{user_id}', response_model=UserDataSchema)
async def get_data_user(user_id: int, session: SessionDB):
    if user := await session.scalar(select(UserModel).where(UserModel.id == user_id)):
        return user

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Такого пользователя не существует!')


@router.get(path='/', response_model=UserDataSchema)
async def get_my_data(request: Request, session: SessionDB):
    if user_id := request.cookies.get('id'):
        if user := await session.scalar(select(UserModel).where(UserModel.id == int(user_id))):
            return user

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Такого пользователя не существует!')

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Вы еще не авторизовались!')
