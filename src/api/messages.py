from fastapi import APIRouter, HTTPException, Request, Depends, status
from typing import Annotated

from src.api.dependecies import messages_service, users_service
from src.services.users import UsersService
from src.services.messages import MessagesService
from src.schemas.messages import MessageAddSchema


router = APIRouter(prefix='/chat', tags=['Chat'])

UsersService = Annotated[UsersService, Depends(users_service)]
MessagesService = Annotated[MessagesService, Depends(messages_service)]


@router.post(path='/new_message')
async def add_message(data: MessageAddSchema, request: Request, users_service: UsersService, messages_service: MessagesService):
    if (user_id := request.cookies.get('id')) is not None:
        if (user := await users_service.get_user_is_id(int(user_id))) is not None:
            if messages_service.add_new_message(user.name, data):
                return {'message': 'Сообщение отправлено!'}

            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Сообщение не было отправлено!')

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Такого пользователя не существует!')

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Вы еще не авторизовались!')


@router.get(path='/messages')
async def get_messages(messages_service: MessagesService):
    if (messages := messages_service.get_messages()) is not None:
        return messages

    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='Сообщения не были загружены!')
