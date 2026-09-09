# Objective: Implement complex processing workflows based on task fulfillment conditions.
import asyncio
from time import ctime

async def network_probe(server_name, delay):
    await asyncio.sleep(delay)
    return f"Ping successful: {server_name}"

async def main():
    # asyncio.wait() allows you to wait for a collection of tasks to complete based on specific conditions, such as waiting for the first task to finish.
    tasks = {
        asyncio.create_task(network_probe("Primary-Server", 2.0)),
        asyncio.create_task(network_probe("Backup-Server-1", 0.5)),
        asyncio.create_task(network_probe("Backup-Server-2", 1.0))
    }
    
    # 
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    
    print(f"{ctime()} Count of Tasks Done: {len(done)}")       # Expected output: 1
    print(f"{ctime()} Count of Tasks Pending: {len(pending)}") # Expected output: 2

    for finished_task in done:
        print(f"{ctime()} Fastest Task Result: {finished_task.result()}")
        
    # Cancel the remaining pending tasks
    for ongoing_task in pending:
        ongoing_task.cancel()

asyncio.run(main())