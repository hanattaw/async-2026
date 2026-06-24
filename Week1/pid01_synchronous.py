from time import sleep, ctime, time
import os
import threading

# Function to simulate making coffee for one customer synchronously
def make_coffee(customer_name):
    # Get the Process ID (PID) and Thread ID (TID)
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] Making coffee for customer {customer_name}...")
    sleep(5)  # Block this thread for 5 seconds to simulate making coffee
    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] Customer {customer_name} has received the coffee!")


def main():
    # Customer queue
    queue = ["A", "B", "C"]

    # Get the main process ID and main thread ID
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] === Starting Synchronous Coffee Simulation ===")

    start_time = time()

    # Serve customers one at a time in queue order
    for customer in queue:
        make_coffee(customer)

    duration = time() - start_time
    print(f"{ctime()} | Total execution time: {duration:.2f} seconds")


if __name__ == "__main__":
    main()