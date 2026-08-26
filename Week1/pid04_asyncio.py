from time import ctime, time
import asyncio
import os
import threading

# ฟังก์ชันจำลองการทำกาแฟแบบ Asynchronous
async def make_coffee(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    
    current_thread_name = threading.current_thread().name
    task_name =asyncio.current_task().get_name()

    task_id = id(asyncio.current_task())

    print(f"[{ctime()}] Process ID: {pid}, Thread ID: {thread_id}, Thread Name: {current_thread_name}, Task Name: {task_name}, Task ID: {task_id} - กำลังทำกาแฟให้ลูกค้า {customer_name}...")
    await asyncio.sleep(5)  # จำลองเวลาที่ใช้ในการทำกาแฟ
    print(f"[{ctime()}] Process ID: {pid}, Thread ID: {thread_id}, Thread Name: {current_thread_name}, Task Name: {task_name}, Task ID: {task_id} - ทำกาแฟให้ลูกค้า {customer_name} เสร็จแล้ว!")

async def main():
    queue = ["A", "B", "C"]
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id
    main_thread_name = threading.current_thread().name
    start_time = time()

    print(f"[{ctime()}] Main Process ID: {main_pid}, Main Thread ID: {main_tid}, Main Thread Name: {main_thread_name} - เริ่มทำงานจำลองตู้กาแฟแบบ Asynchronous...")
    start_time = time()
    

    tasks = []
    for customer in queue:
        task = asyncio.create_task(make_coffee(customer), name=f"CoffeeTask-{customer}")
        tasks.append(task)

    await asyncio.gather(*tasks)

    duration = time() - start_time
    print(f"[{ctime()}] Main Process ID: {main_pid}, Main Thread ID: {main_tid}, Main Thread Name: {main_thread_name} - ทำงานเสร็จแล้ว! ใช้เวลาทั้งหมด: {duration:.2f} วินาที")
    
if __name__ == "__main__":
    asyncio.run(main())