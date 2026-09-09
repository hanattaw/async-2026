# Program 6: Creating a Concurrent Task
# Concept: Wrapping a coroutine inside asyncio.create_task() to schedule it to run in the background.
import asyncio
from os import name
from time import time, ctime

async def cook_spaghetti(CUSTOMER_NAME):
    print(f"{ctime()} Strat Cooking spaghetti for {CUSTOMER_NAME}!")
    await asyncio.sleep(2)  # Simulate cooking time
    print(f"{ctime()} finished cooking for customer {CUSTOMER_NAME}!")

async def main():
    start_time = time()
    # Create a concurrent task for cooking spaghetti for customer A
    task_a = asyncio.create_task(cook_spaghetti("A"))
    print(f"{ctime()} Task created for customer A")
    await task_a  # Await the completion of the task for customer A

   
    end_time = time()
    print(f"Total operation time: {end_time - start_time} seconds")

if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine using the event loop