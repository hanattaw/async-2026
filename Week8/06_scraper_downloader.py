import asyncio

async def link_scraper(queue: asyncio.Queue, page_urls: list):
    """Producer: สแกนหาลิงก์รูปภาพแล้วใส่ลง Queue"""
    print("[Producer] เริ่มสแกนหาลิงก์รูปภาพ...")

    for page in page_urls:
        print(f"  -- [Producer] สแกนหน้าเว็บ: {page}")
        await asyncio.sleep(0.3)  # จำลองการดาวน์โหลด HTML

        # แก้ไขการใช้ตัวแปรใน f-string ให้ถูกต้อง
        img_url_1 = f"https://example.com/images/{page}_img1.jpg"
        img_url_2 = f"https://example.com/images/{page}_img2.jpg"

        await queue.put(img_url_1)
        await queue.put(img_url_2)

    print("[Producer] สแกนหาลิงก์รูปภาพเสร็จสิ้น!\n")

async def image_downloader(queue: asyncio.Queue, worker_name: str):
    """Consumer: ดึงลิงก์รูปภาพจาก Queue แล้วดาวน์โหลด"""
    downloaded_count = 0
    print(f"[{worker_name}] สตาร์ทเตรียมพร้อมโหลดรูป...")

    while True:
        # ดึงลิงก์รูปภาพจาก Queue
        img_url = await queue.get()

        # ตรวจสอบสัญญาณหยุด (Sentinel Value)
        if img_url is None:
            queue.task_done()
            break

        downloaded_count += 1
        print(f"  -> [{worker_name}] (รูปที่ {downloaded_count}) กำลังโหลด: {img_url}")
        await asyncio.sleep(0.5)  # จำลองเวลาดาวน์โหลดรูป

        # แจ้งว่าประมวลผลรูปเสร็จแล้ว
        queue.task_done()

    print(f"[{worker_name}] ทำงานเสร็จสิ้น! ดาวน์โหลดรวมทั้งหมด {downloaded_count} รูป")

async def main():
    pages = ["page_1", "page_2", "page_3"]
    queue = asyncio.Queue()

    # 1. สร้าง Task สำหรับ Producer และ Consumer (1 ตัว)
    producer_task = asyncio.create_task(link_scraper(queue, pages))
    downloader_task = asyncio.create_task(image_downloader(queue, "Downloader_01"))

    # 2. รอให้ Producer ทำงานเสร็จ
    await producer_task

    # 3. รอให้ Consumer ประมวลผลรูปใน Queue จนหมด
    await queue.join()

    # 4. ส่ง None 1 ครั้ง เพื่อแจ้งให้ Downloader ตัวเดียวนี้หยุดทำงาน
    await queue.put(None)
    await downloader_task

if __name__ == "__main__":
    asyncio.run(main())