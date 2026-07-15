from time import ctime, time, process_time
import asyncio
import os
import threading
import psutil

# ฟังก์ชันจำลองการทำกาแฟแบบ Asynchronous
async def make_coffee(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().name
    current_task = asyncio.current_task()
    task_name = current_task.get_name() if current_task else 'Task'
    print(f"{ctime()} | [PID: {pid}] [Task: {task_name}] Making coffee for {customer_name}...")
    await asyncio.sleep(1)
    print(f"{ctime()} | [PID: {pid}] [Task: {task_name}] Coffee ready for {customer_name}!")
    print(f"{ctime()} | [PID: {pid}] [Task: {task_name}] LCD: Processing for customer {customer_name}...")
    await asyncio.sleep(1)
    print(f"{ctime()} | [PID: {pid}] [Task: {task_name}] LCD: Done for customer {customer_name}.")

async def main():
    queue = ['A', 'B', 'C']
    proc = psutil.Process(os.getpid())
    print(f"{ctime()} | [Main PID: {os.getpid()}] === Asyncio (ps) ===")
    start = time()
    cpu_start = process_time()

    tasks = [asyncio.create_task(make_coffee(c), name=f"Task-{c}") for c in queue]
    await asyncio.gather(*tasks)

    cpu_end = process_time()
    duration = time() - start
    print(f"{ctime()} | [Summary] Wall Time: {duration:.2f} seconds")
    print(f"{ctime()} | [Summary] CPU Time: {cpu_end - cpu_start:.4f} seconds")
    print(f"{ctime()} | [Summary] Memory (RSS): {proc.memory_info().rss / (1024*1024):.2f} MB")

if __name__ == "__main__":
    asyncio.run(main())
    