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
        await asyncio.sleep(0.04)

    print(f"[{consumer_name}] ทำงานเสร็จสิ้น! รวมคูปองที่เก็บได้ทั้งหมด {len(claimed_coupons)} ใบ -> {claimed_coupons}")
    return claimed_coupons

async def main():
    TOTAL_COUPONS = 20
    NUM_CONSUMERS = 2
    queue = asyncio.Queue()

    # 1. สร้าง Task สำหรับ Producer 
    prod_task = asyncio.create_task(producer(queue, TOTAL_COUPONS))

    # 2. สร้าง Task สำหรับ consumer 2 ตัวรันขนานกัน 
    consumers = [
        asyncio.create_task(consumer(queue, f'Consumer_{i:02d}'))
        for i in range(1, NUM_CONSUMERS + 1)
    ]

    # 3. รอให้ Producer สร้างคูปองเสร็จ
    await prod_task

    # 4. รอให้ Consumer ทั้ง 2 ตัวช่วยกันรุมเครียร์คูปงใน Queue จนหมด
    await queue.join()

    # 5. ส่ง sentinel value [None] เท่ากันจำนวน Consumer (2 อัน) เพื่อหยุด consumer ทุกตัว
    for _ in range(NUM_CONSUMERS):
        await queue.put(None)

    # 6. รอให้ consumer ทุกตัวทำงานสมบูรณ์
    await asyncio.gather(*consumers)
    print("\n=== ระบบประมวลผลคูปองแบบ Multi-Consumer ทำงานเสร็จสิ่นทั้งหมด ===")
if __name__ == "__main__":
    asyncio.run(main())