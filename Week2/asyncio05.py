# Program 5: Sequential Execution (The Wrong Way)
# Concept: Showing that simply awaiting one after another is still sequential (Synchronous behavior).
import asyncio
from os import name
from time import time,ctime

async def serve_customer(name):
    print(f"{ctime()} Cooking for {name}!")
    await asyncio.sleep(2)  # Simulate cooking time
    print(f"{ctime()} serve {name}!")

async def main():
    start_time = time()
    await serve_customer("A")  # Awaiting the first customer
    await serve_customer("B")  # Awaiting the second customer
    end_time = time()
    print(f"Total time taken: {end_time - start_time} seconds")

if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine using the event loop