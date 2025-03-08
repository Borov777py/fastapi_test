from typing import Annotated
from fastapi import Depends

from services.users import UsersService
from services.messages import MessagesService


UsersService = Annotated[UsersService, Depends(lambda: UsersService)]
MessagesService = Annotated[MessagesService, Depends(lambda: MessagesService)]
