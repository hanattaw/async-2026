import asyncio
import aiohttp
import time

BASE_URL = "http://172.16.2.117:8088/api"
STUDENT_ID = "6710301027"

lights = [
    "light_1",
    "light_2",
    "light_3",
    "light_4"
]

async def turn_on_light(session, light):
    print(f"กำลังเปิด {light}...")

    async with session.post(
        f"{BASE_URL}/{STUDENT_ID}/lights/{light}",
        json={"status": "ON"}
    ) as response:

        data = await response.json()
        print(data)

async def main():

    start = time.perf_counter()

    async with aiohttp.ClientSession() as session:

        tasks = [
            turn_on_light(session, light)
            for light in lights
        ]

        await asyncio.gather(*tasks)

    end = time.perf_counter()

    print("-" * 40)
    print(f"ใช้เวลาทั้งหมด: {end - start:.2f} วินาที")

asyncio.run(main())