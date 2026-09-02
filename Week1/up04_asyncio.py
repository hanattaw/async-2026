from time import ctime, time
import asyncio

# Simulate LCD screen update
async def update_cup_number(customer_name):
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    await asyncio.sleep(1) # Non-blocking wait
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")

# Simulate making coffee
async def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    await asyncio.sleep(1) # Non-blocking wait
    print(f"{ctime()} | Coffee ready for {customer_name}!")

# Combined task for each customer
async def serve_customer(customer_name):
    await make_coffee(customer_name)
    await update_cup_number(customer_name)

async def main():
    print(f"{ctime()} | === Asyncio Coffee Machine ===")
    
    start_time = time()
    queue = ['A', 'B', 'C']
    tasks = []

    # Create and schedule tasks
    for customer in queue:
        task = asyncio.create_task(serve_customer(customer))
        tasks.append(task)

    # Run tasks concurrently
    await asyncio.gather(*tasks)

    # Calculate total duration
    total_time = time() - start_time
    print(f"{ctime()} | Total time: {total_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())