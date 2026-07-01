# Program: Restaurant Operation (Asyncio Refactored)
# Concept: Mixing sequential execution (greeting) with concurrent tasks using asyncio, utilizing consistent function names.
import asyncio
from time import time, ctime

# 1. ขั้นตอนต้อนรับหน้าร้าน ทำแบบ Sequential (รอทีละคนจนเสร็จ)
async def greet_diners(customer):
    print(f"{ctime()} Greeting for {customer} ...")
    await asyncio.sleep(1)
    print(f"{ctime()} Greeting for {customer} ...Done!")

# 2. กระบวนการส่วนตัวของลูกค้าแต่ละคน ที่จะถูกนำไปโยนเข้า Task ให้ทำขนานกัน
async def customer_private_workflow(task_id):
    # Take Order
    print(f"{ctime()} [{task_id}] Taking Order ...")
    await asyncio.sleep(1)
    print(f"{ctime()} [{task_id}] Taking Order ...Done!")

    # Do Cooking
    print(f"{ctime()} [{task_id}] Cooking Spaghetti ...")
    await asyncio.sleep(1)
    print(f"{ctime()} [{task_id}] Cooking Spaghetti ...Done!")

    # Manage Bar
    print(f"{ctime()} [{task_id}] Manage Bar for Drink ...")
    await asyncio.sleep(1)
    print(f"{ctime()} [{task_id}] Manage Bar for Drink ...Done!")
    print(f"{ctime()} [{task_id}] All served!\n")

async def main():
    customers = ['Customer-A', 'Customer-B', 'Customer-C']
    task_ids = ['Task-A', 'Task-B', 'Task-C']
    
    start_time = time()

    # ---------------------------------------------------------
    # PHASE 1: Greet ลูกค้าทีละคนแบบ Synchronous ด้วยการ await ทีละคำสั่ง
    # ---------------------------------------------------------
    for customer in customers:
        await greet_diners(customer)

    print(f"\n{ctime()} --- All customers greeted. Scheduling independent Async Tasks! ---\n")

    # ---------------------------------------------------------
    # PHASE 2: สร้าง Task ให้ลูกค้าแต่ละคนไปทำกระบวนการที่เหลือขนานกัน
    # ---------------------------------------------------------
    tasks = []
    for task_id in task_ids:
        # ใช้ asyncio.create_task แทน threading.Thread หรือ multiprocessing.Process
        t = asyncio.create_task(customer_private_workflow(task_id))
        tasks.append(t)

    # รอให้ทุก Task ในลิสต์ทำงานของตัวเองเสร็จสิ้นทั้งหมด
    for t in tasks:
        await t

    duration = time() - start_time
    print(f"{ctime()} Finished Entire Restaurant Operation in {duration:.2f} seconds.")

if __name__ == "__main__":
    # จุดเริ่มต้นรัน Event Loop ของ asyncio
    asyncio.run(main())