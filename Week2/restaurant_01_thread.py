import threading
from time import ctime,time,sleep

def greet_dinner(customer):
    print(f'{ctime} Greeting for customer-{customer}...')
    sleep(1)
    print(f'{ctime} Greeting for customer-{customer}...Done!')

def customer_private_workflow(customer):

    print(f'{ctime} [Thread-{customer}] Taking Order ...')
    sleep(1)
    print(f'{ctime} [Thread-{customer}] Taking Order ...Done!')

    print(f'{ctime} [Thread-{customer}] Cooking ...')
    sleep(1)
    print(f'{ctime} [Thread-{customer}] Cooking ...Done!')

    print(f'{ctime} [Thread-{customer}] Mini Bar ...')
    sleep(1)
    print(f'{ctime} [Thread-{customer}] Mini Bar ...Done!')

if __name__ == "__main__":
    customers = ["A","B","C","D"]
    start_time = time()

    for customer in customers:
        greet_dinner(customer)
    print(f'\n{ctime()} --- All customer greet')

    duration = time() -start_time
    print(f'{ctime} Finished Entire Restaurant Operation in {duration:.2f} second')


