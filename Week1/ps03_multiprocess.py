from time import sleep, ctime, time, process_time
import multiprocessing
import threading
import os
import psutil

# ฟังก์ชันสำหรับชงกาแฟเสิร์ฟลูกค้าแต่ละคิว
def make_coffee(customer_name, result_queue):
    # หาค่า Process ID ปัจจุบัน (แต่ละโพรเซสจะรันแยกกันและมีค่าไม่ซ้ำกัน)
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] กำลังชงกาแฟให้ ลูกค้า {customer_name}...")
    start_cpu = process_time()
    sum(i * i for i in range(1000000)) # สร้างโหลดให้ CPU ทำงานเพื่อจำลองการประมวลผลจริง
    sleep(5) # หน่วงเวลาไว้ 5 วินาที (จำลองระยะเวลาการรอเครื่องชงกาแฟ)
    cpu_duration = process_time() - start_cpu
    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")

    # นำข้อมูลการใช้แรมและเวลา CPU ของตัวเอง ส่งคืนไปยังโปรแกรมหลักผ่าน Queue
    process = psutil.Process(pid)
    mem_mb = process.memory_info().rss / (1024 * 1024)
    result_queue.put((mem_mb, cpu_duration))

def main():
    queue = ['A', 'B', 'C']
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] === เริ่มระบบจำลองตู้กาแฟแบบ Multi-processing ===")
    start_time = time()
    main_start_cpu = process_time()

    result_queue = multiprocessing.Queue()
    processes = []
    
    # วนลูปเพื่อจัดการคิวลูกค้าตามลำดับ
    for customer in queue:
        # แตกโพรเซสย่อยใหม่สำหรับลูกค้าแต่ละคนอย่างเป็นอิสระ
        p = multiprocessing.Process(target=make_coffee, args=(customer, result_queue))
        processes.append(p)
        p.start()

    # ดึงข้อมูลทรัพยากรที่ถูกส่งมาจากโพรเซสลูกทั้งหมด
    child_memories = []
    child_cpu_times = []
    for _ in queue:
        mem, cpu_t = result_queue.get()
        child_memories.append(mem)
        child_cpu_times.append(cpu_t)

    for p in processes:
        p.join()

    duration = time() - start_time

    # ตรวจสอบการใช้ RAM ของตัวโปรแกรมหลัก (Main Process) เองด้วย
    main_process = psutil.Process(os.getpid())
    main_mem = main_process.memory_info().rss / (1024 * 1024)

    total_memory = main_mem + sum(child_memories)
    total_cpu_time = (process_time() - main_start_cpu) + sum(child_cpu_times)

    print(f"[สรุปผล Multi-processing]")
    print(f"เวลาที่ใช้จริง (Wall Time): {duration:0.2f} วินาที")
    print(f"เวลารวมที่ CPU ทุก Core ช่วยกันประมวลผล (Total CPU Time): {total_cpu_time:0.4f} วินาที")
    print(f"ทรัพยากร Memory (RAM) รวมทุก Process: {total_memory:.2f} MB (Main: {main_mem:.2f} MB + ย่อย: {sum(child_memories):.2f} MB)")

if __name__ == "__main__":
    main()