from time import sleep, ctime, time, process_time
import threading
import os
import psutil

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คน
def make_coffee(customer_name):
    pid = os.getpid()
    tid = threading.current_thread().name
    print(f"{ctime()} | [PID: {pid}] [Thread: {tid}] Making coffee for {customer_name}...")
    sleep(1)
    print(f"{ctime()} | [PID: {pid}] [Thread: {tid}] Coffee ready for {customer_name}!")
    print(f"{ctime()} | [PID: {pid}] [Thread: {tid}] LCD: Processing for customer {customer_name}...")
    sleep(1)
    print(f"{ctime()} | [PID: {pid}] [Thread: {tid}] LCD: Done for customer {customer_name}.")

def main():
    queue = ['A', 'B', 'C']
    proc = psutil.Process(os.getpid())
    print(f"{ctime()} | [Main PID: {os.getpid()}] === Multi-thread (ps) ===")
    start = time()
    cpu_start = process_time()

    threads = []
    for c in queue:
        t = threading.Thread(target=make_coffee, args=(c,), name=f"Thread-{c}")
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    cpu_end = process_time()
    duration = time() - start
    print(f"{ctime()} | [Summary] Wall Time: {duration:.2f} seconds")
    print(f"{ctime()} | [Summary] CPU Time: {cpu_end - cpu_start:.4f} seconds")
    print(f"{ctime()} | [Summary] Memory (RSS): {proc.memory_info().rss / (1024*1024):.2f} MB")

if __name__ == "__main__":
    main()