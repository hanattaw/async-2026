# Program 9: Dynamically Tracking Tasks in a List
# Concept: Managing multiple generated tasks dynamically by appending them into a standard Python list.
import asyncio
from time import time, ctime

async def serve_customer(name):
    print(f"{ctime()} -> Handling customer {name}")
    await asyncio.sleep(1)  # Simulating a time-consuming task
    print(f"{ctime()} -> Done customer {name}")

async def main():
    start_time = time()
    customers = ["A", "B", "C", "D"]  # List of customers to serve
    task_list = []  # List to hold all the tasks

    # Dynamically creating and appending tasks to the list
    for customer in customers:
        t = asyncio.create_task(serve_customer(name))
        task_list.append(t)


    for t in task_list:
        await t  # Awaiting each task to ensure they complete before moving on

    print(f"Served all {len(customers)} customers in {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())