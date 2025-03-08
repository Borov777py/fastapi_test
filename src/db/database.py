from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import PG_URL

engine = create_async_engine(url=PG_URL)

new_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass
