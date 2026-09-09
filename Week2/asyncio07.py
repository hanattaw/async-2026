# Program 7: Dual Tasks Concurrency
# Concept: Scheduling two distinct tasks concurrently and awaiting them individually without gather.
import asyncio
from time import time,ctime

async def cook_spaghetti(customer):
    print(f"{ctime()} Start cooking spaghetti for {customer}!")
    await asyncio.sleep(2)  # Simulate cooking time
    print(f"{ctime()} Finished cooking spaghetti for {customer}!")

async def main():
    start_time = time()
    # Schedule two distinct tasks concurrently
    task_a = asyncio.create_task(cook_spaghetti("A"))
    task_b = asyncio.create_task(cook_spaghetti("B"))
    
    print(f"{ctime()} Tasks created for customers A and B")
    
    # Await the completion of both tasks individually
    await task_a
    await task_b
    
    end_time = time()
    print(f"Total operation time: {end_time - start_time} seconds")

if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine using the event loop