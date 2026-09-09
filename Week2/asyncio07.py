# Program 7: Dual Tasks Concurrency
# Concept: Scheduling two distinct tasks concurrently and awaiting them individually without gather.
import asyncio
from time import time, ctime

async def Cook_spaghetti(name):
    print(f"{ctime()} -> Cooking spaghetti for {name}")
    await asyncio.sleep(1)  # Simulate a delay in cooking
    print(f"{ctime()} - Finished cooking spaghetti for {name}")


async def main():
    start_time = time()

    # Creating tasks for each customer
    task_a = asyncio.create_task(Cook_spaghetti("A"))
    task_b = asyncio.create_task(Cook_spaghetti("B"))

    print(f"{ctime()} -> Starting cooking tasks")

    # Awaiting the tasks individually
    await task_a  # Awaiting the first task
    await task_b  # Awaiting the second task

    print(f"Total Operation Time: {time() - start_time:.2} seconds")


if __name__ == "__main__":
    asyncio.run(main())  # Run the coroutine object using the event loop

