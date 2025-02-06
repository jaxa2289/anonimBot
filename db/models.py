import asyncio

from sqlalchemy import String, DECIMAL, select, ForeignKey, BigInteger, Boolean
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from db import Base, db
from db.utils import CreatedModel


class User(CreatedModel):
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    chat_id: Mapped[int] = mapped_column(BigInteger,unique=True,nullable=False)
    status: Mapped[bool] = mapped_column(Boolean, nullable=False,default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Pair(CreatedModel):
    __tablename__ = "juftlars"
    chat_id_1:Mapped[int] = mapped_column(BigInteger, ForeignKey('users.chat_id'), nullable=False)
    chat_id_2:Mapped[int] = mapped_column(BigInteger, ForeignKey('users.chat_id'), nullable=False)

    status: Mapped[bool] = mapped_column(Boolean, nullable=False)
    user1 = relationship('User', foreign_keys=[chat_id_1])
    user2 = relationship('User', foreign_keys=[chat_id_2])





metadata = Base.metadata



