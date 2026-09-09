from time import ctime, time
import asyncio
import os
import threading

# ฟังก์ชันจำลองการทำกาแฟแบบ Asynchronous
async def make_coffee(customer_name):
    #1 ดู Process ID และ Thread ID (ซึ่งจะพบว่าเหมือนกันทุกคิว)
    pid = os.getpid()
    thread_id = threading.current_thread().native_id

    #2 ดูข้อมูล task ปัจจุบันของ asyncio
    current_task = asyncio.current_task()
    task_name  = current_task.get_name() # ชื่อ taks
    
    task_id = id(current_task)

    print(f"{ctime()}| [PID: {pid}] [TID: {thread_id}] [Async Task ID: {task_id}] [Task Name: {task_name}] กำลังชงกาแฟให้ ลูกค้า {customer_name}..." )
    await  asyncio.sleep(5) #บล็อกการทำงานของ thread นี้ไว้ 5 วินาที
    print(f"{ctime()}| [PID: {pid}] [TID: {thread_id}] [Async Task ID: {task_id}] [Task Name: {task_name}] ลูกค้า {customer_name} ได้รับกาแฟแล้ว!" )
    pass   

async def main():
    # คิวลูกค้า
    queue = {'A','B','C'}
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] === เริ่มระบบจำลองตู้กาแฟแบบ asyncio ===")
    start_time = time()

    tasks = []
    # ลูปทำงานตามลำดับคิวเดียว (ทีละคน)
    for customer in queue:
        #สร้าง task ใหม่แยกจากกันเด็ดขาด
        coro = make_coffee(customer)
        #แปลง Corotine ให้เป็น task  เพื่อให้ event loop บริหาร และตั้งชื่อได้
        task = asyncio.create_task(coro, name=f'Task-{customer}')
        tasks.append(task)
        
    await asyncio.gather(*tasks)
    duration = time() - start_time
    print(f"{ctime()} | ใช้เวลารวมทั้งหมด: {duration:.2f} วินาที")

    pass

if __name__ == "__main__":
    asyncio.run(main())