# Objective: Learn how to query the lifecycle status of a task object.
import asyncio
from time import ctime

async def short_job():
    await asyncio.sleep(1)
    return "Success"

async def main():
    task = asyncio.create_task(short_job())
    
    # Inspect status immediately while the task is still running
    print(f"{ctime()} Is task done? {task.done()}")          # Expected output: False
    print(f"{ctime()} Is task canceled? {task.cancelled()}")  # Expected output: False
    
    await task # wait for the task to complete
    
    # Inspect status again after it finishes
    print(f"{ctime()} Is task done now? {task.done()}")      # Expected output: True
    print(f"{ctime()} Is task canceled now? {task.cancelled()}") # Expected output: False

asyncio.run(main())