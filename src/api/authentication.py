from fastapi import APIRouter, HTTPException, Response, Depends, status
from hashlib import sha256

from src.schemas.users import UserAuthSchema
from src.services.users import UsersService
from src.api.dependecies import users_service


router = APIRouter(prefix='/auth', tags=['Authentication'])


@router.post(path='/registration')
async def registration(data: UserAuthSchema, users_service: UsersService = Depends(users_service)):
    if await users_service.get_user_is_name(data.name) is None:
        data.password = sha256(data.password.encode()).hexdigest()
        await users_service.add_user(data)
        return {'message': 'Вы успешно зарегистрировались!'}

    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Имя пользователя занято!')


@router.post(path='/authorization')
async def authorization(data: UserAuthSchema, response: Response, users_service: UsersService = Depends(users_service)):
    if (user := await users_service.get_user_is_name(data.name)) is not None:
        hash_password = sha256(data.password.encode()).hexdigest()
        if user.password == hash_password:
            response.set_cookie('id', user.id)
            return {'message': 'Вы успешно авторизовались!'}

        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Не верный пароль!')

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Такого пользователя не существует!')
