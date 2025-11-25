from models import Animals
from settings import Base, async_engine, async_session
import asyncio

async def create_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def insert_data():
    async with async_session() as session:
        async with session.begin():
            animals1 = Animals(name="Pug",age=3)
            animals2 = Animals(name="Buldog",age=5,adoped=True)
            session.add_all([animals1, animals2])
            await session.commit()


async def main():
    await create_db()
    print("Database and tables created.")
    await insert_data()
    print("Sample data inserted.")


if __name__ == "__main__":
    asyncio.run(main())
