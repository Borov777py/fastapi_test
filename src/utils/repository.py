from sqlalchemy import select


from db.database import new_session


class Repository:
    def __init__(self, model: ...):
        self.model = model

    async def get_one_is_id(self, id_: int):
        async with new_session() as session:
            result = await session.scalar(select(self.model).where(self.model.id == id_))
        return result

    async def get_one_is_name(self, name: str):
        async with new_session() as session:
            result = await session.scalar(select(self.model).where(self.model.name == name))
        return result

    async def add_one(self, data: dict):
        async with new_session() as session:
            session.add(self.model(**data))
            await session.commit()
