from time import sleep, ctime, time, process_time
import threading
import os
import psutil

# Function to simulate LCD screen update
def update_cup_number(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    sum(i * i for i in range(1000000)) # Simulate CPU processing
    sleep(1) # Takes 1 second to update
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")

# Function to simulate making coffee
def make_coffee(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"{ctime()} | Making coffee for {customer_name}...")
    sum(i * i for i in range(1000000)) # Simulate CPU processing
    sleep(1) # Takes 1 second to brew
    print(f"{ctime()} | Coffee ready for {customer_name}!")

# Wrapper function for each thread to execute (make coffee then update LCD)
def serve_customer(customer_name):
    make_coffee(customer_name)
    update_cup_number(customer_name)

def main():
    queue = ['A', 'B', 'C']
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(f"{ctime()} | === Multi-threading Coffee Machine ===")
    
    start_time = time()
    start_cpu = process_time()

    threads = []
    # Loop to create a thread for each customer (start concurrently)
    for customer in queue:
        # Assign serve_customer function to the thread
        t = threading.Thread(target=serve_customer, args=(customer,), name=f"Thread-{customer}")
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Summary of results
    duration = time() - start_time
    cpu_duration = process_time() - start_cpu
    
    process = psutil.Process(os.getpid())
    mem_mb = process.memory_info().rss / (1024 * 1024)

    #print(f"\n[Summary Multi-threading]")
    print(f"Total Wall Time: {duration:0.2f} seconds")
    print(f"Total CPU Time: {cpu_duration:0.4f} seconds")
    print(f"Total Memory (RAM): {mem_mb:.2f} MB")

if __name__ == "__main__":
    main()