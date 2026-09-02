# Program 7: Dual Tasks Concurrency
# Concept: Scheduling two distinct tasks concurrently and awaiting them individually without gather.
import asyncio
from time import time, ctime

async def cook_spaghetti(customer):
    print(f"{ctime()} -> Starting to cook for Customer {customer}...")
    await asyncio.sleep(1)  # Simulating a time-consuming task
    print(f"{ctime()} -> Starting to cook for Customer {customer}!")

async def main():
    start_time = time()


    task_a = asyncio.create_task(cook_spaghetti("A"))
    task_b = asyncio.create_task(cook_spaghetti("B"))


    await task_a  # This will pause the main coroutine until Task A is complete.
    await task_b  # This will pause the main coroutine until Task B is complete.


    print(f"Total Operation Time: {time() - start_time:.2f} seconds")
    
if __name__ == "__main__":
    asyncio.run(main())