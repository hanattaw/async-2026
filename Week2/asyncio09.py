# Program 9: Dynamically Tracking Tasks in a List
# Concept: Managing multiple generated tasks dynamically by appending them into a standard Python list.
import asyncio
from time import time, ctime

async def serve_customer(customer_name):
    print(f"{ctime()} Start serving customer {customer_name}!")
    await asyncio.sleep(1)  # Simulate serving time
    print(f"{ctime()} Finished serving customer {customer_name}!")

async def main():
    start_time = time()
    tasks = []  # สร้างลิสต์ชื่อ tasks

    for name in customer:
        t = asyncio.create_task(serve_customer(name))  # Create a task for each customer
        tasks.append(t)  # แก้ไขจาก task_list เป็น tasks

    for t in tasks:  # แก้ไขจาก task_list เป็น tasks
        await t  # Await the completion of each task

    print(f"Served {len(customer)} customers in {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    customer = ["A", "B", "C", "D"]  # List of customers
    asyncio.run(main())  # Run the main coroutine using the event loop