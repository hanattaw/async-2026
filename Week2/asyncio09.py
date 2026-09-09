# Program 9: Dynamically Tracking Tasks in a List
# Concept: Managing multiple generated tasks dynamically by appending them into a standard Python list.
import asyncio
from time import time, ctime

async def serve_customer():
    print(f"{ctime()} -> Handling customer ")
    await asyncio.sleep(1)  # Simulate a delay in serving
    print(f"{ctime()} - Done customer")

async def main():
    start_time = time()
    customers = ["A", "B", "C"]  # List of customers
    tasks_list = []  # List to hold the tasks

    # Dynamically creating and appending tasks to the list
    for name in customers:
        t = asyncio.create_task(serve_customer())
        tasks_list.append(t)

    print(f"{ctime()} -> Starting to serve customers")

    # Awaiting all tasks in the list
    for t in tasks_list:
        await t

    print(f"Total Operation Time: {time() - start_time:.2} seconds")

if __name__ == "__main__":
    asyncio.run(main())  # Run the coroutine object using the event loop

