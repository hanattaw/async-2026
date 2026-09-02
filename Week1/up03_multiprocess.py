from time import sleep, ctime, time, process_time
import multiprocessing
import threading
import os
import psutil

# ฟังก์ชันจำลองการอัปเดตหน้าจอ LCD
def update_cup_number(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    sum(i * i for i in range(1000000)) # จำลองการทำงาน CPU
    sleep(1) # ใช้เวลาอัปเดต 1 วินาที
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")

# ฟังก์ชันจำลองการชงกาแฟ
def make_coffee(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    
    print(f"{ctime()} | Making coffee for {customer_name}...")
    sum(i * i for i in range(1000000)) # จำลองการทำงาน CPU
    sleep(1) # ใช้เวลาชง 1 วินาที
    print(f"{ctime()} | Coffee ready for {customer_name}!")

# ฟังก์ชันตัวกลางเพื่อรวบงานให้ Process ย่อยทำงานรวดเดียวและเก็บค่า RAM/CPU ส่งกลับ
def serve_customer(customer_name, result_queue):
    start_cpu = process_time()
    
    make_coffee(customer_name)
    update_cup_number(customer_name)
    
    cpu_duration = process_time() - start_cpu
    process = psutil.Process(os.getpid())
    mem_mb = process.memory_info().rss / (1024 * 1024)
    
    # ส่งข้อมูล RAM และ CPU ของโพรเซสนี้กลับไปยังโปรแกรมหลัก
    result_queue.put((mem_mb, cpu_duration))

def main():
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id
    print(f"{ctime()} | === Multi-processing Coffee Machine ===")
    
    start_time = time()
    main_start_cpu = process_time()

    queue = ['A', 'B', 'C']
    result_queue = multiprocessing.Queue()
    processes = []

    # เริ่มสร้าง Process ย่อยให้ลูกค้าทุกคนพร้อมกัน
    for customer in queue:
        p = multiprocessing.Process(target=serve_customer, args=(customer, result_queue))
        processes.append(p)
        p.start()

    # รับข้อมูลทรัพยากรที่ส่งกลับมาจากโพรเซสย่อย
    child_memories = []
    child_cpu_times = []
    for _ in queue:
        mem, cpu_t = result_queue.get()
        child_memories.append(mem)
        child_cpu_times.append(cpu_t)

    # รอให้ทุก Process ย่อยทำงานจนเสร็จสมบูรณ์
    for p in processes:
        p.join()

    duration = time() - start_time
    
    # คำนวณ RAM ของโปรแกรมหลัก
    main_process = psutil.Process(os.getpid())
    main_mem = main_process.memory_info().rss / (1024 * 1024)
    
    total_memory = main_mem + sum(child_memories)
    total_cpu_time = (process_time() - main_start_cpu) + sum(child_cpu_times)

    #print(f"\n[Summary Multi-processing]")
    print(f"Total Wall Time: {duration:0.2f} seconds")
    print(f"Total CPU Time: {total_cpu_time:0.4f} seconds")
    print(f"Total Memory (RAM): {total_memory:.2f} MB (Main: {main_mem:.2f} MB + Child: {sum(child_memories):.2f} MB)")

if __name__ == "__main__":
    main()