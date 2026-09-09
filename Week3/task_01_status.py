# Objective: Learn how to query the lifecycle status of a task object.
import asyncio
from time import ctime

async def short_job():
    await asyncio.sleep(1)
    return "Success"

async def main():
    #Create a task object to run the short_job coroutine
    task = asyncio.create_task(short_job())
    
    # Check the status of the task before it finishes
    print(f"{ctime()} Is task done? {task.done()}")#Expected: False
    print(f"{ctime()} Is task canceled? {task.cancelled()}")  #Expected: False
    
    await task #Await here for the task to finish, but the callback will be triggered automatically when it does
    
    # Inspect status again after it finishes
    print(f"{ctime()} Is task done now? {task.done()}")      # Expected: True
    print(f"{ctime()} Is task canceled now? {task.cancelled()}") # Expected: False

asyncio.run(main())