"""
โปรแกรมเปิดไฟทั้งหมด - แบบ ASYNCHRONOUS (พร้อมกันทุกดวง)
=========================================================

ส่ง request เปิดไฟทั้ง 4 ดวงพร้อมกันด้วย asyncio.gather
โดยเรียก control_light() จาก lab_utils.py
-> เวลารวม ≈ ค่า delay ที่มากที่สุดในกลุ่ม (ไม่ใช่ผลรวม)

เวลาที่คาดว่าจะใช้ ≈ max(0.5, 1.2, 2.0, 0.8) = 2.0 วินาที
"""

import asyncio
import time

from light_utils import control_light, BASE_URL

STUDENT_ID = "6710301025"  
LIGHT_IDS = ["light_1", "light_2", "light_3", "light_4"]


async def async_turn_on_all(student_id: str = STUDENT_ID):
    print("== เปิดไฟพร้อมกันทั้งหมด (async) ==")
    start = time.perf_counter()

    tasks = [
        control_light(student_id, light_id, "ON")
        for light_id in LIGHT_IDS
    ]
    results = await asyncio.gather(*tasks)

    elapsed = time.perf_counter() - start

    for light_id, result in zip(LIGHT_IDS, results):
        if result.get("status") == "ERROR":
            print(f"  {light_id}: ล้มเหลว -> {result['detail']}")
        else:
            print(f"  {light_id}: {result['current_status']}")

    print(f"เสร็จสิ้น ใช้เวลาทั้งหมด {elapsed:.2f} วินาที")


if __name__ == "__main__":
    asyncio.run(async_turn_on_all())