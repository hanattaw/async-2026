import asyncio

async def producer(queue: asyncio.Queue, total_coupons: int):
    """Producer: สร้างคูปอง 20 ใบแล้วดันลง asyncio.Queue"""
    print(f"[Producer] เริ่มสร้างคูปองจำนวน {total_coupons} ใบ...")

    for i in range(1,total_coupons +1):
        coupon = f"COUPON-{i:02d}"
        await queue.put(coupon)
        print(f"  -- [Producer] สร้างและใส่คิวสำเร็จ: {coupon}")
        await asyncio.sleep(0.02)  # จำลองการดาวน์โหลด HTML

    print("[Producer] สร้างคูปองเสร็จสิ้นเรียบร้อยแล้ว!\n")

async def consumer(queue: asyncio.Queue, consumer_name: str):
    """Consumer: 1 ตัวมีหน้าที่ดึงคูปองออกจาก asyncio.Queue มาเก็บไว้"""
    claimed_coupons = []
    print(f"[{consumer_name}] เริ่มต้นรอคูปอง...")

    while True:
        # ดึงลิงก์รูปภาพจาก Queue
        coupon = await queue.get()

        # ตรวจสอบสัญญาณหยุด (Sentinel Value)
        if coupon is None:
            queue.task_done()
            break

        claimed_coupons.append(coupon)
        print(f"  -> [{consumer_name} ได้รับคูปอง: {coupon} (รวมสะสม: {len(claimed_coupons)} ใบ")
        
        # แจ้งว่าประมวลผลรูปเสร็จแล้ว
        queue.task_done()
        await asyncio.sleep(0.05)

    print(f"[{consumer_name}] ทำงานเสร็จสิ้น! รวมคูปองที่เก็บได้ทั้งหมด {len(claimed_coupons)} ใบ")
    print(f"รายการคูปอง: {claimed_coupons}")

async def main():
    TOTAL_COUPONS = 20
    queue = asyncio.Queue()

    # 1. สร้าง Task สำหรับ Producer และ Consumer (1 ตัว)
    prod_task = asyncio.create_task(producer(queue, TOTAL_COUPONS))
    cons_task = asyncio.create_task(consumer(queue, "Consumer_01"))

    # 2. รอให้ Producer ทำงานเสร็จ
    await prod_task

    # 3. รอให้ Consumer ประมวลผลรูปใน Queue จนหมด
    await queue.join()

    # 4. ส่ง None 1 ครั้ง เพื่อแจ้งให้ Downloader ตัวเดียวนี้หยุดทำงาน
    await queue.put(None)
    await cons_task

if __name__ == "__main__":
    asyncio.run(main())