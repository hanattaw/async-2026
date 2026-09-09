# Objective: Attach a plain synchronous function that automatically triggers the moment a task finishes.
import asyncio
from time import ctime

def alert_manager(finished_task):
    # Callback function automatically accepts the completed task object as its only argument
    print(f"{ctime()} Callback Triggered! Task output fetched: {finished_task.result()}")

async def download_file():
    print(f"{ctime()} Downloading packet...")
    await asyncio.sleep(1.0)
    return "Data_Payload.zip"

async def main():
    task = asyncio.create_task(download_file())
    # Register the callback function (Do not add parentheses '()' )
    task.add_done_callback(alert_manager)
    
    await task # Wait for the task to complete

asyncio.run(main())