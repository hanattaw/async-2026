import asyncio
import multiprocessing
from time import ctime, sleep, time

def greet_dinner(customer):
    print(f"{ctime()} Greeting for Customer-{customer} ...")
    sleep(1)  # Simulate a delay in greeting
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")

def customer_private_workflow(customer):
    print(f"{ctime()} Taking Order for Customer-{customer} ...")
    sleep(1)  # Simulate a delay in taking order
    print(f"{ctime()} Taking Order for Customer-{customer} ...Done!")


    print(f"{ctime()} Cooking for Customer-{customer} ...")
    sleep(1)  # Simulate a delay in cooking
    print(f"{ctime()} Cooking for Customer-{customer} ...Done!")


    print(f"{ctime()} Mini bar for Customer-{customer} ...")
    sleep(1)  # Simulate a delay in preparing mini bar
    print(f"{ctime()} Mini bar for Customer-{customer} ...Done!")

if __name__ == "__main__":
    customers = ["A", "B", "C"]
    start_time = time()

    for customer in customers:
        greet_dinner(customer)

    print(f"\n{ctime()} --- All customer greeted. FORKING into independent processes (Branching) ---")

    processes = []
    for customer in customers:
        p = multiprocessing.Process(target=customer_private_workflow, args=(customer,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()

    duration = time() - start_time
    print(f"{ctime()} finished cooking in {duration:.2f} seconds")
