# Objective: Extract returned data safely and inspect crashed tasks without breaking the main loop.
import asyncio
from time import ctime

async def division_worker(a, b):
    await asyncio.sleep(0.5)
    return a / b # 

async def main():
    task_success = asyncio.create_task(division_worker(10, 2))
    task_fail = asyncio.create_task(division_worker(10, 0))#Exception 

    # Wait for a while to let the tasks finish (or crash)
    await asyncio.sleep(1)
    
    # Retrieve the value using.result() safely for the successful task
    if task_success.done() and not task_success.exception():
        print(f"{ctime()} Task Success Result: {task_success.result()}") # 
        
    # Retrieve the exception using .exception() safely for the failed task
    if task_fail.done(): 
        print(f"{ctime()} Task Fail Exception: {type(task_fail.exception()).__name__}") # 

asyncio.run(main())