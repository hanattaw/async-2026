# Program 8: Task Interleaving (Context Switching)
# Concept: Watching a single thread switch back and forth between two different workflows using create_task.
import asyncio
from time import time, ctime

async def kitchen_crew():
    print(f"{ctime()} [Chef] puts noodle in boiling water!")
    await asyncio.sleep(1)  # Simulate preparation time
    print(f"{ctime()} [Chef] has finished cooking the noodles!")

async def bar_crew():
    print(f"{ctime()} [Barista] is ready to serve drinks!")
    await asyncio.sleep(1)  # Simulate preparation time
    print(f"{ctime()} Bar crew has finished serving drinks!")

async def main():
    task_kitchen = asyncio.create_task(kitchen_crew())
    task_bar = asyncio.create_task(bar_crew())  
    # Await the completion of both tasks
    await task_kitchen
    await task_bar


    
if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine using the event loop