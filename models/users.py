from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from db.database import Base
from schemas.users import UserDataSchema


class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(35), unique=True)
    password: Mapped[str] = mapped_column(String())
    balance: Mapped[int] = mapped_column(default=0)

    def read_model(self) -> UserDataSchema:
        return UserDataSchema(id=self.id,
                              name=self.name,
                              password=self.password,
                              balance=self.balance)
