from src.services.users import UsersService
from src.services.messages import MessagesService
from src.models.users import UserModel
from src.utils.storage import Storage


def users_service():
    return UsersService(UserModel)


def messages_service():
    return MessagesService(Storage)
