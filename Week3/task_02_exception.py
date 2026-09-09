# Objective: Extract returned data safely and inspect crashed tasks without breaking the main loop.
import asyncio
from time import ctime

async def division_worker(a, b):
    await asyncio.sleep(0.5)
    return a / b # will raise ZeroDivisionError if b == 0

async def main():
    task_success = asyncio.create_task(division_worker(10, 2))
    task_fail = asyncio.create_task(division_worker(10, 0))

    # wait for both tasks to finalize operations
    await asyncio.sleep(1)
    
    # Rewrite successful value .result()
    if task_success.done() and not task_success.exception():
        print(f"{ctime()} Task Success Result: {task_success.result()}") # Expected output: 5.0
        
    # Inspect failed task .exception()
    if task_fail.done():
        print(f"{ctime()} Task Fail Exception: {type(task_fail.exception()).__name__}") # Expected output: ZeroDivisionError

asyncio.run(main())