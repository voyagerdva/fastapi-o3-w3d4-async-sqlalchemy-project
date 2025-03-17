import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from database.engine import engine

async def test_connection():
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT 1"))
        print("ОК. Подключение успешно!", result.scalar())

if __name__ == '__main__':
    asyncio.run(test_connection())