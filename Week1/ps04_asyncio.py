from time import ctime, time, process_time
import asyncio
import os
import threading
import psutil

# ฟังก์ชันชงกาแฟแบบทำงานสลับกันไปมาโดยไม่รอ (Asynchronous)
async def make_coffee(customer_name):
    # ดึงค่า PID และ TID (สังเกตว่าในระบบ Asyncio จะใช้แค่ Process และ Thread เดียวกันทั้งหมด)
    pid = os.getpid()
    thread_id = threading.current_thread().native_id

    # ดึงข้อมูลของ Task ปัจจุบันที่กำลังรันอยู่ และดูชื่อของ Task
    current_task = asyncio.current_task()
    task_name = current_task.get_name()

    # สร้าง ID ตัวเลขเฉพาะตัวของแต่ละ Task เพื่อให้แยกแยะง่ายขึ้น (รองรับ Python 3.12+)
    task_id = id(current_task)

    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Async Task ID: {task_id}] [Task Name: {task_name}] กำลังชงกาแฟให้ ลูกค้า {customer_name}...")
    
    # โค้ดถ่วงเวลาจำลองการใช้พลังงาน CPU ประมวลผลนิดหน่อย
    sum(i * i for i in range(1000000)) 
    
    # จุดสำคัญ (Non-blocking wait): หน่วงเวลา 5 วินาที
    # ระหว่างที่หน่วงเวลานี้ ระบบจะไม่รอเฉยๆ แต่จะสลับคิวไปชงให้ลูกค้าคนอื่นก่อน!
    await asyncio.sleep(5)
    
    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Async Task ID: {task_id}] [Task Name: {task_name}] ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")

async def main():
    queue = ['A', 'B', 'C']
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] === เริ่มระบบจำลองตู้กาแฟแบบ asyncio ===")
    start_time = time()
    start_cpu = process_time()

    tasks = []
    # วนลูปรายชื่อลูกค้าในคิว
    for customer in queue:
        # เตรียมออร์เดอร์กาแฟของแต่ละคน
        coro = make_coffee(customer)
        # แพ็กออร์เดอร์เป็น "Task" ส่งให้ระบบ Asyncio คอยสลับคิวจัดการ พร้อมตั้งชื่อให้ดูง่าย
        task = asyncio.create_task(coro, name=f"Task-{customer}")
        tasks.append(task)

    # สั่งให้ทุก Task เริ่มทำงานไปพร้อมๆ กัน และหยุดรอตรงนี้จนกว่าจะเสร็จครบทุกคน
    await asyncio.gather(*tasks)

    duration = time() - start_time
    cpu_duration = process_time() - start_cpu

    # ตรวจสอบว่าโปรแกรมนี้กิน RAM ไปเท่าไหร่
    process = psutil.Process(os.getpid())
    mem_mb = process.memory_info().rss / (1024 * 1024)

    print(f"[สรุปผล Asyncio]")
    print(f"เวลาที่ใช้จริง (Wall Time): {duration:0.2f} วินาที")
    print(f"เวลาที่ CPU ใช้ประมวลผลจริง (CPU Time): {cpu_duration:0.4f} วินาที")
    print(f"ทรัพยากร Memory (RAM) ที่ใช้: {mem_mb:.2f} MB")

if __name__ == "__main__":
    # จุดเริ่มต้นรันโปรแกรมแบบ Asynchronous
    asyncio.run(main())