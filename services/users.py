from schemas.users import UserAuthSchema, UserDataSchema
from db.database import Repository
from models.users import UserModel


class UsersService:
    repository = Repository(UserModel)

    @classmethod
    async def add_user(cls, data: UserAuthSchema):
        data_dict = data.model_dump()
        await cls.repository.add_one(data_dict)

    @classmethod
    async def get_user_is_id(cls, id_: int):
        result = await cls.repository.get_one_is_id(id_)
        return result

    @classmethod
    async def get_user_is_name(cls, name: str):
        result = await cls.repository.get_one_is_name(name)
        return result
