import asyncio
import httpx
from time import ctime


async def fetch_stock_price(server_name: str):
    """
    TODO: Assignment 3 - เขียนฟังก์ชันเชื่อมต่อ Mock Server ผ่านระบบเครือข่าย
    1. กำหนดเป้าหมายไปที่พอร์ต 8088 ตามสเปกเซิร์ฟเวอร์ของอาจารย์
    2. ใช้ httpx.AsyncClient() ดึงข้อมูลเพื่อไม่ให้เกิดการ Block สัญญาณ Event Loop
    3. นำข้อมูล JSON (server และ price_usd) มาจัดฟอร์แมตแสดงผล
    """
    url = f"http://172.16.2.117:8088/price/{server_name}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()
        return f"[{data['server']}] Price: {data['price_usd']} USD"


async def main():
    tasks = {
        asyncio.create_task(fetch_stock_price("Alpha"), name="Alpha"),
        asyncio.create_task(fetch_stock_price("Beta"), name="Beta"),
        asyncio.create_task(fetch_stock_price("Gamma"), name="Gamma"),
    }

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    winner_task = next(iter(done))
    print(f"{ctime()} Winner Result: {winner_task.result()}")

    print(f"{ctime()} Cleaning up {len(pending)} pending tasks...")
    for ongoing_task in pending:
        ongoing_task.cancel()

    await asyncio.gather(*pending, return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(main())