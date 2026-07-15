# Asyncio version of the simple restaurant workflow
import asyncio
from time import ctime, time

async def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer} ...")
    await asyncio.sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")

async def take_orders(customer):
    print(f"{ctime()} Taking Order for Customer-{customer} ...")
    await asyncio.sleep(1)
    print(f"{ctime()} Taking Order for Customer-{customer} ...Done!")

async def do_cooking(customer):
    print(f"{ctime()} Cooking for Customer-{customer} ...")
    await asyncio.sleep(1)
    print(f"{ctime()} Cooking for Customer-{customer} ...Done!")

async def mini_bar(customer):
    print(f"{ctime()} Mini Bar for Customer-{customer} ...")
    await asyncio.sleep(1)
    print(f"{ctime()} Mini Bar for Customer-{customer} ...Done!")

async def serve_customer(customer):
    await greet_diners(customer)
    await take_orders(customer)
    await do_cooking(customer)
    await mini_bar(customer)

async def main():
    customers = ['A', 'B', 'C']
    start_time = time()

    await asyncio.gather(*(serve_customer(customer) for customer in customers))

    duration = time() - start_time
    print(f"{ctime()} Finished Cooking in {duration:0.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())