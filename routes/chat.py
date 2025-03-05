from fastapi import APIRouter, HTTPException, status, Request
from sqlalchemy import select

from database import SessionDB, UserModel, get_data_messages, add_new_message
from schemas.messages import MessageAddSchema


router = APIRouter(prefix='/chat', tags=['Chat'])


@router.post(path='/new_message')
async def add_message(data: MessageAddSchema, request: Request, session: SessionDB):
    if user_id := request.cookies.get('id'):
        if user := await session.scalar(select(UserModel).where(UserModel.id == int(user_id))):
            if add_new_message(f'{user.name}: {data.message}'):
                return {'message': 'Сообщение отправлено!'}

            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Сообщение не было отправлено!')

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Такого пользователя не существует!')

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Вы еще не авторизовались!')


@router.get(path='/messages')
async def get_messages():
    if messages := get_data_messages():
        return messages

    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='Сообщения не были загружены!')


