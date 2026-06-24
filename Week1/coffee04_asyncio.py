from time import ctime, time
import asyncio

# ฟังก์ชันจำลองการทำกาแฟแบบ Asynchronous
async def make_coffee(customer_name):
    print(f"{ctime()} กำลังชงกาแฟให้ ลูกค้า {customer_name}...")
    await asyncio.sleep(1) # จำลองเวลาชงกาแฟ 1 วินาที
    print(f"{ctime()} ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")

async def main():
    # คิวลูกค้า
    queue = ['A', 'B', 'C']
    print(f"{ctime()} === เริ่มระบบจำลองตู้กาแฟแบบ asyncio ===")
    start_time = time()
    
    # รวบรวม Task
    tasks = [make_coffee(customer) for customer in queue]
    await asyncio.gather(*tasks)
    
    duration = time() - start_time
    print(f"{ctime()} ลูกค้า {len(queue)} คน ใช้เวลา: {duration:0.2f} วินาที")

# สั่งให้ระบบ Async เริ่มทำงาน
if __name__ == "__main__":
    # ใช้ asyncio.run เพื่อเปิด Event Loop หลักของโปรแกรม
    asyncio.run(main())