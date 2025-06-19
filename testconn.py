import asyncpg
import asyncio

async def test_connection():
    conn = await asyncpg.connect(
        user="postgres",
        password="7870",
        database="fastapi_restaurant",
        host="localhost"
    )
    print("✅ Подключение успешно!")
    await conn.close()

asyncio.run(test_connection())