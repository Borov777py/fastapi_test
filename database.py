import json
from sqlalchemy.ext.asyncio import AsyncAttrs, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, String, ForeignKey
from typing import Annotated
from fastapi import Depends
from redis import Redis

from config import PG_URL, REDIS_HOST, REDIS_PASSWORD

redis_ = Redis(REDIS_HOST, 6379, password=REDIS_PASSWORD, decode_responses=True)

engine = create_async_engine(url=PG_URL)

new_session = async_sessionmaker(engine)


def get_data_messages():
    if data := redis_.get('messages'):
        try:
            return json.loads(data)
        except:
            pass
    return None


def add_new_message(message: str):
    if messages := get_data_messages():
        messages.append(message)
        redis_.set('messages', json.dumps(messages))
        return True
    return False


async def get_session():
    async with new_session() as session:
        yield session


SessionDB = Annotated[AsyncSession, Depends(get_session)]


class Base(AsyncAttrs, DeclarativeBase):
    pass


class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(35), unique=True)
    password: Mapped[str] = mapped_column(String())
    balance: Mapped[int] = mapped_column(default=0)

