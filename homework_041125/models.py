from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import String
from settings import Base, config

class Animals(Base):
    __tablename__ = "animals"

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name: Mapped[str] = mapped_column(String(50),nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    adoped: Mapped[bool] = mapped_column(default=False)
