import os
import dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

dotenv.load_dotenv()


class Config:
    DATABASE_NAME = os.getenv("DATABASE_NAME", "database_cafe_frutige_aero")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    def uri_postgres(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@localhost:5432/{self.DATABASE_NAME}"

    def uri_sqlite(self):
        return "sqlite+aiosqlite:///./test.db"
    
    def alembic_uri_sqlite(self):
        return f"sqlite:///./{self.DATABASE_NAME}.db"
    
api_config = Config()

async_engine = create_async_engine(api_config.uri_sqlite(), echo=True)
async_session = async_sessionmaker(bind=async_engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


# Dependency: сесія БД для FastAPI
async def get_db():
    async with async_session() as session:
        yield session