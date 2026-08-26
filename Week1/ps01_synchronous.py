from time import sleep, ctime, time, process_time
import os
import threading
import psutil


# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คนแบบซิงโครนัส
def make_coffee(customer_name):
    pid = os.getpid()
    thread = threading.current_thread().name
    print(f"{ctime()} | [PID: {pid}] [Thread: {thread}] Making coffee for {customer_name}...")
    sleep(1)
    print(f"{ctime()} | [PID: {pid}] [Thread: {thread}] Coffee ready for {customer_name}!")
    print(f"{ctime()} | [PID: {pid}] [Thread: {thread}] LCD: Processing for customer {customer_name}...")
    sleep(1)
    print(f"{ctime()} | [PID: {pid}] [Thread: {thread}] LCD: Done for customer {customer_name}.")

def main():
    queue = ['A', 'B', 'C']
    proc = psutil.Process(os.getpid())
    print(f"{ctime()} | [Main PID: {os.getpid()}] === Synchronous (ps) ===")
    start = time()
    cpu_start = process_time()

    for c in queue:
        make_coffee(c)

    cpu_end = process_time()
    duration = time() - start
    print(f"{ctime()} | [Summary] Wall Time: {duration:.2f} seconds")
    print(f"{ctime()} | [Summary] CPU Time: {cpu_end - cpu_start:.4f} seconds")
    mem_mb = proc.memory_info().rss / (1024 * 1024)
    print(f"{ctime()} | [Summary] Memory (RSS): {mem_mb:.2f} MB")

if __name__ == "__main__":
    main()
    