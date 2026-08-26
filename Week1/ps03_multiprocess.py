from time import sleep, ctime, time, process_time
import multiprocessing
import threading
import os
import psutil

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คน
def make_coffee(customer_name, result_queue):
    pid = os.getpid()
    print(f"{ctime()} | [PID: {pid}] Making coffee for {customer_name}...")
    sleep(1)
    print(f"{ctime()} | [PID: {pid}] Coffee ready for {customer_name}!")
    print(f"{ctime()} | [PID: {pid}] LCD: Processing for customer {customer_name}...")
    sleep(1)
    print(f"{ctime()} | [PID: {pid}] LCD: Done for customer {customer_name}.")
    # report memory usage back to parent
    try:
        proc = psutil.Process(pid)
        mem = proc.memory_info().rss
    except Exception:
        mem = 0
    result_queue.put((pid, mem))

def main():
    queue = ['A', 'B', 'C']
    print(f"{ctime()} | [Main PID: {os.getpid()}] === Multi-process (ps) ===")
    start = time()
    cpu_start = process_time()

    processes = []
    result_q = multiprocessing.Queue()
    for c in queue:
        p = multiprocessing.Process(target=make_coffee, args=(c, result_q))
        processes.append(p)
        p.start()

    total_child_mem = 0
    for p in processes:
        p.join()

    # collect reported memory
    while not result_q.empty():
        pid, mem = result_q.get()
        total_child_mem += mem

    cpu_end = process_time()
    duration = time() - start
    main_mem = psutil.Process(os.getpid()).memory_info().rss
    total_mem_mb = (main_mem + total_child_mem) / (1024*1024)
    print(f"{ctime()} | [Summary] Wall Time: {duration:.2f} seconds")
    print(f"{ctime()} | [Summary] CPU Time: {cpu_end - cpu_start:.4f} seconds")
    print(f"{ctime()} | [Summary] Total Memory (main+children RSS): {total_mem_mb:.2f} MB")

if __name__ == "__main__":
    main()
    