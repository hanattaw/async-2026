from time import sleep, ctime, time, process_time
import os
import threading
import psutil

# Function to simulate LCD screen update
def update_cup_number(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    sum(i * i for i in range(1000000)) # Simulate CPU work
    sleep(1) # Update takes 1 second
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")

# Function to simulate making coffee
def make_coffee(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"{ctime()} | Making coffee for {customer_name}...")
    sum(i * i for i in range(1000000)) # Simulate CPU work
    sleep(1) # Brewing takes 1 second
    print(f"{ctime()} | Coffee ready for {customer_name}!")

def main():
    queue = ['A', 'B', 'C']
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(f"{ctime()} | === Synchronous Coffee Machine ===")
    
    # Start timer
    start_time = time()
    start_cpu = process_time()

    # Sequential execution loop (must finish one task before moving to the next)
    for customer in queue:
        make_coffee(customer)       # Step 1: Make coffee
        update_cup_number(customer) # Step 2: Update LCD

    # Calculate final duration and memory usage
    duration = time() - start_time
    cpu_duration = process_time() - start_cpu
    
    process = psutil.Process(os.getpid())
    mem_mb = process.memory_info().rss / (1024 * 1024)

    #print(f"\n[Summary Synchronous]")
    print(f"Total Wall Time: {duration:0.2f} seconds")
    print(f"Total CPU Time: {cpu_duration:0.4f} seconds")
    print(f"Total Memory (RAM): {mem_mb:.2f} MB")

if __name__ == "__main__":
    main()