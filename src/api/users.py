from fastapi import APIRouter, HTTPException, Request, status

from src.api.dependencies import UsersService
from src.schemas.users import UserDataSchema


router = APIRouter(prefix='/user', tags=['User'])


@router.get(path='/{user_id}', response_model=UserDataSchema)
async def get_data_user(user_id: int, users_service: UsersService):
    if (user := await users_service.get_user_is_id(user_id)) is not None:
        return user

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Такого пользователя не существует!')


@router.get(path='/', response_model=UserDataSchema)
async def get_my_data(request: Request, users_service: UsersService):
    if (user_id := request.cookies.get('id')) is not None:
        if (user := await users_service.get_user_is_id(int(user_id))) is not None:
            return user

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Такого пользователя не существует!')

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Вы еще не авторизовались!')
