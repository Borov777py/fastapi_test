from fastapi import APIRouter, HTTPException, status, Response
from sqlalchemy import select
from hashlib import sha256

from database import SessionDB, UserModel
from schemas.users import UserAuthSchema

router = APIRouter(prefix='/auth', tags=['Authentication'])


@router.post(path='/registration')
async def registration(data: UserAuthSchema, session: SessionDB):
    if not await session.scalar(select(UserModel).where(UserModel.name == data.name)):
        hash_password = sha256(data.password.encode()).hexdigest()
        session.add(UserModel(name=data.name, password=hash_password))
        await session.commit()
        return {'message': 'Вы успешно зарегистрировались!'}

    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Имя пользователя занято!')


@router.post(path='/authorization')
async def authorization(data: UserAuthSchema, session: SessionDB, response: Response):
    if user := await session.scalar(select(UserModel).where(UserModel.name == data.name)):
        hash_password = sha256(data.password.encode()).hexdigest()
        if user.password == hash_password:
            response.set_cookie('id', user.id)
            return {'message': 'Вы успешно авторизовались!'}

        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Не верный пароль!')

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Такого пользователя не существует!')
