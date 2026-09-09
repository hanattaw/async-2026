# Program 4: The await Keyword
# Concept: Pausing a coroutine to let another operation finish using await.
import asyncio
from time import ctime

async def main():
    print(f"{ctime()}")

    await asyncio.sleep(1)  # Simulate a delay
    
    print(f"{ctime()}")


if __name__ == "__main__":
    asyncio.run(main())  # Run the coroutine object using the event loop
