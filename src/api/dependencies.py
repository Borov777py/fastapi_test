from typing import Annotated
from fastapi import Depends

from src.services.users import UsersService
from src.services.messages import MessagesService
from src.models.users import UserModel
from src.utils.storage import Storage


UsersService = Annotated[UsersService, Depends(lambda: UsersService(UserModel))]
MessagesService = Annotated[MessagesService, Depends(lambda: MessagesService(Storage))]
