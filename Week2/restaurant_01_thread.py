from time import sleep, ctime, time
import threading


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

    print(f"\n{ctime()} --- All customer greeted. Splitting into individual threads1 ---")


    customer_threads = []
    for customer in customers:
        t = threading.Thread(target=customer_private_workflow, args=(customer,))
        customer_threads.append(t)
        t.start()

    for t in customer_threads:
        t.join()


duration = time() - start_time
print(f"{ctime()} finished cooking in {duration:.2f} seconds")