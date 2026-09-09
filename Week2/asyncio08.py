# Program 8: Task Interleaving (Context Switching)
# Concept: Watching a single thread switch back and forth between two different workflows using create_task.
import asyncio
from time import time, ctime

async def kitchen_Crew(name):
    print(f"{ctime()} -> [Chef]  puts noodle in boiling water...")
    await asyncio.sleep(1)  # Simulate a delay in cooking
    print(f"{ctime()} - [Chef]strains the noodle!")

async def bar_Crew(name):
    print(f"{ctime()} -> [Bar]  starts grinding the coffee beans...")
    await asyncio.sleep(1)  # Simulate a delay in preparing the drink
    print(f"{ctime()} - [Bar]  pour esspresso shot!")


async def main():
    start_time = time()

    # Creating tasks for each crew
    task_kitchen = asyncio.create_task(kitchen_Crew("Kitchen"))
    task_bar = asyncio.create_task(bar_Crew("Bar"))

    print(f"{ctime()} -> Starting kitchen and bar tasks")

    # Awaiting the tasks individually
    await task_kitchen  # Awaiting the kitchen task
    await task_bar      # Awaiting the bar task

    print(f"Total Operation Time: {time() - start_time:.2} seconds")


if __name__ == "__main__":
    asyncio.run(main())  # Run the coroutine object using the event loop

