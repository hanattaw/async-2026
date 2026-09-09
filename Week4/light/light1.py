"""
โปรแกรมเปิดไฟทั้งหมด - แบบ SYNCHRONOUS (ทีละดวง)
=================================================

เปิดไฟทีละดวงตามลำดับโดยเรียก control_light() จาก lab_utils.py
แต่ละดวงต้องรอ hardware delay ให้เสร็จก่อน ถึงจะไปเปิดดวงถัดไปได้
-> เวลารวม = ผลรวมของ delay ทุกดวง

เวลาที่คาดว่าจะใช้ = 0.5 + 1.2 + 2.0 + 0.8 = 4.5 วินาที

หมายเหตุ: control_light() เป็น async function เท่านั้น
จึงต้องใช้ asyncio.run() เรียกทีละครั้งเพื่อจำลองพฤติกรรมแบบ sync
"""

import asyncio
import time

from light_utils import control_light, BASE_URL, reset_all_lights


STUDENT_ID = "6710301025"   # <-- แก้เป็นรหัสนักศึกษาของคุณ
LIGHT_IDS = ["light_1", "light_2", "light_3", "light_4"]


def sync_turn_on_all(student_id: str = STUDENT_ID):
    """
    print("== ปิดไฟพร้อมกันทั้งหมด (async) ==")

    # reset lights before running tasks
    reset_all_lights(student_id)
    """
    print("== เปิดไฟทีละดวง (sync) ==")
    start = time.perf_counter()

    for light_id in LIGHT_IDS:
        # เรียกทีละครั้ง รอผลลัพธ์เสร็จก่อนถึงจะไปดวงถัดไป
        result = asyncio.run(control_light(student_id, light_id, "ON"))

        if result.get("status") == "ERROR":
            print(f"  {light_id}: ล้มเหลว -> {result['detail']}")
        else:
            print(f"  {light_id}: {result['current_status']}")

    elapsed = time.perf_counter() - start
    print(f"เสร็จสิ้น ใช้เวลาทั้งหมด {elapsed:.2f} วินาที")


if __name__ == "__main__":
    sync_turn_on_all()