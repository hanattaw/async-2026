
import asyncio
from time import ctime, time

cup_number = 0

async def update_cup_number(customer_name):
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    await asyncio.sleep(1)
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")

async def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    await asyncio.sleep(1)
    print(f"{ctime()} | Coffee ready for {customer_name}!")
    await update_cup_number(customer_name)

async def main():
    queue = ['A', 'B', 'C']
    print(f"{ctime()} | === Asyncio Coffee Machine ===")
    start_time = time()
    tasks = [make_coffee(customer) for customer in queue]
    await asyncio.gather(*tasks)
    duration = time() - start_time
    print(f"{ctime()} | Total time: {duration:0.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())