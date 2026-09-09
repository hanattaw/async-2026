# foodcourt_02_gather.py
import asyncio
import time
from time import ctime
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301025"
    print(f"{ctime()} | --- [Task 2] Practice using gather to wait for all group orders ---")

    start = time.perf_counter()

    # 1) สร้าง coroutine สำหรับ 3 ออเดอร์
    orders = [
        send_order_to_kitchen(MY_STUDENT_ID, "hainanese_chicken", "Chicken Rice Mixed"),
        send_order_to_kitchen(MY_STUDENT_ID, "noodle", "Wonton Noodles"),
        send_order_to_kitchen(MY_STUDENT_ID, "steak", "Sizzling Steak"),
    ]

    # 2) รันทั้ง 3 ออเดอร์พร้อมกัน แล้วรอผลลัพธ์ทั้งหมด
    results = await asyncio.gather(*orders)

    # 3) แสดงผลแต่ละจานที่ได้รับ
    for res in results:
        print(f"{ctime()} | [Pickup] Shop: {res['shop']} | Menu: {res['menu']} is ready!")

    elapsed = time.perf_counter() - start
    print(f"{ctime()} | Total time: {elapsed:.2f} seconds (Equals to the slowest dish).")

if __name__ == "__main__":
    asyncio.run(main())