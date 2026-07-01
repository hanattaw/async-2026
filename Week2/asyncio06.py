# Program 6: Creating a Concurrent Task
# Concept: Wrapping a coroutine inside asyncio.create_task() to schedule it to run in the background.
import asyncio
from time import time, ctime

async def cook_spaghetti(customer):
    print(f"{ctime()} -> Starting to cook for Customer {customer}...")
    await asyncio.sleep(1)  # Simulating a time-consuming task
    print(f"{ctime()} -> Starting to cook for Customer {customer}!")

async def main():
    start_time = time()


    task_a = asyncio.create_task(cook_spaghetti("A"))

    print(f"{ctime()} Main program can do other things while Task A is running in the background.")


    await task_a  # This will pause the main coroutine until Task A is complete.

    print(f"Total Operation Time: {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())