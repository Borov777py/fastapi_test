from fastapi import APIRouter, HTTPException, Request, status

from api.dependencies import MessagesService, UsersService
from schemas.messages import MessageAddSchema


router = APIRouter(prefix='/chat', tags=['Chat'])


@router.post(path='/new_message')
async def add_message(data: MessageAddSchema, request: Request, users_service: UsersService, messages_service: MessagesService):
    if (user_id := request.cookies.get('id')) is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Вы еще не авторизовались!')

    if (user := await users_service.get_user_is_id(int(user_id))) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Такого пользователя не существует!')

    if messages_service.add_new_message(user.name, data) is False:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Сообщение не было отправлено!')

    return {'message': 'Сообщение отправлено!'}


@router.get(path='/messages')
async def get_messages(messages_service: MessagesService):
    if (messages := messages_service.get_messages()) is None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='Сообщения не были загружены!')
    return messages
