import asyncio
from time import ctime,time,sleep

def greet_dinner(customer):
    print(f'{ctime} Greeting for customer-{customer}...')
    sleep(1)
    print(f'{ctime} Greeting for customer-{customer}...Done!')

def take_order(customer):
    print(f'{ctime} taking for order-{customer}...')
    sleep(1)
    print(f'{ctime} taking for order-{customer}...Done!')

def do_cooking(customer):
    print(f'{ctime} Cooking for customer-{customer}...')
    sleep(1)
    print(f'{ctime} Cooking for customer-{customer}...Done!')

def mini_bar(customer):
    print(f'{ctime} Mini Bar for customer-{customer}...')
    sleep(1)
    print(f'{ctime} Mini Bar for customer-{customer}...Done!')

if __name__ == "__main__":
    customers = ["A","B","C","D"]
    start_time = time()

    for customer in customers:
        greet_dinner(customer)
        take_order(customer)
        do_cooking(customer)
        mini_bar(customer)

        duration = time() -start_time
        print(f'{ctime} Finished cooking in {duration:.2f} second')


