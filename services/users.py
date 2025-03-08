from typing import Type

from schemas.users import UserAuthSchema, UserDataSchema
from utils.repository import Repository
from models.users import UserModel


class UsersService:
    def __init__(self, model: Type[UserModel]):
        self.repository = Repository(model)

    async def add_user(self, data: UserAuthSchema):
        data_dict = data.model_dump()
        await self.repository.add_one(data_dict)

    async def get_user_is_id(self, id_: int):
        result = await self.repository.get_one_is_id(id_)
        return result

    async def get_user_is_name(self, name: str):
        result = await self.repository.get_one_is_name(name)
        return result
