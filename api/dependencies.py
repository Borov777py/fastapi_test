from typing import Annotated
from fastapi import Depends

from services.users import UsersService
from services.messages import MessagesService
from models.users import UserModel
from utils.storage import Storage


UsersService = Annotated[UsersService, Depends(lambda: UsersService(UserModel))]
MessagesService = Annotated[MessagesService, Depends(lambda: MessagesService(Storage))]
