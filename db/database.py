from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select
from typing import Type
import os

engine = create_async_engine(url=f"postgresql+asyncpg://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}")

new_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Repository:
    def __init__(self, model: Type[Base]):
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
