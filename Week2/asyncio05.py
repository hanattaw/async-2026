# Program 5: Sequential Execution (The Wrong Way)
# Concept: Showing that simply awaiting one after another is still sequential (Synchronous behavior).
import asyncio
from time import ctime, time

async def  serve_customer(name):
    print(f"{ctime()} -> Cooking for {name}")
    await asyncio.sleep(1)  # Simulate a delay in serving the customer
    print(f"{ctime()} - Finished serving customer: {name}")

async def main():
    start = time()

    await serve_customer("A")  # Awaiting the first customer
    await serve_customer("B")    # Awaiting the second customer

    print(f"Total time: {time() - start:.2} seconds")


if __name__ == "__main__":
    asyncio.run(main())  # Run the coroutine object using the event loop