import asyncio
import httpx
import time

BASE_URL = "http://172.16.2.117:8088"
STUDENT_ID = "6720301002"
LIGHT_IDS = ["light_1", "light_2", "light_3", "light_4"]


async def get_lights_status(client: httpx.AsyncClient):
    r = await client.get(f"{BASE_URL}/api/{STUDENT_ID}/lights")
    r.raise_for_status()
    return r.json()


async def control_light_async(client: httpx.AsyncClient, light_id: str, status: str):
    """ควบคุมไฟ 1 ดวง แบบ async — ไม่บล็อก event loop ระหว่างรอ"""
    url = f"{BASE_URL}/api/{STUDENT_ID}/lights/{light_id}"
    payload = {"status": status}
    t0 = time.time()
    r = await client.post(url, json=payload)
    elapsed = time.time() - t0
    r.raise_for_status()
    return light_id, r.json(), elapsed


async def turn_on_all_async():
    """เปิดไฟทุกดวงพร้อมกัน (concurrent)"""
    print("=== [ASYNC] เปิดไฟทุกดวงพร้อมกัน ===")
    start = time.time()
    async with httpx.AsyncClient(timeout=30) as client:
        tasks = [control_light_async(client, lid, "ON") for lid in LIGHT_IDS]
        results = await asyncio.gather(*tasks)
        for light_id, data, elapsed in results:
            print(f"  {light_id}: {data}  (ใช้เวลา {elapsed:.2f}s)")
    total = time.time() - start
    print(f"เวลารวมทั้งหมด: {total:.2f}s\n")
    return total


async def reset_all_async():
    print("=== [ASYNC] Reset ไฟทั้งหมด ===")
    async with httpx.AsyncClient(timeout=30) as client:
        start = time.time()
        r = await client.delete(f"{BASE_URL}/api/{STUDENT_ID}/lights/reset")
        r.raise_for_status()
        elapsed = time.time() - start
        print(f"  response: {r.json()}  (ใช้เวลา {elapsed:.2f}s)\n")


async def main():
    async with httpx.AsyncClient(timeout=30) as client:
        print("สถานะก่อนเริ่ม:", await get_lights_status(client))
    await reset_all_async()
    await turn_on_all_async()
    async with httpx.AsyncClient(timeout=30) as client:
        print("สถานะหลังทำ:", await get_lights_status(client))


if __name__ == "__main__":
    asyncio.run(main())