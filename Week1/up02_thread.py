from time import sleep, ctime, time
import threading

lock = threading.Lock()

def update_cup_number(customer_name):
    with lock:
        print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    sleep(1)
    with lock:
        print(f"{ctime()} | LCD: Done for customer {customer_name}.")

def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    sleep(1)
    print(f"{ctime()} | Coffee ready for {customer_name}!")
    update_cup_number(customer_name)

def main():
    queue = ['A', 'B', 'C']
    print(f"{ctime()} | === Multi-threading Coffee Machine ===")
    start = time()
    threads = []
    for c in queue:
        t = threading.Thread(target=make_coffee, args=(c,), name=f"Thread-{c}")
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"{ctime()} | Total time: {time() - start:.2f} seconds")

if __name__ == "__main__":
    main()