from time import sleep, ctime, time, process_time
import threading
import os
import psutil

# ฟังก์ชันสำหรับจำลองขั้นตอนการชงกาแฟเสิร์ฟลูกค้าแต่ละคิว
def make_coffee(customer_name):
    # ตรวจสอบ Process ID ปัจจุบัน (ทุกเธรดจะแชร์ PID เดียวกันหมด)
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] กำลังชงกาแฟให้ ลูกค้า {customer_name}...")
    sum(i * i for i in range(1000000)) # สร้างภาระให้ CPU ประมวลผลเล่นๆ เพื่อจำลองการทำงาน
    sleep(5) # หน่วงเวลาเธรดปัจจุบันไว้ 5 วินาที (จำลองเวลาชงกาแฟ)
    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")

def main():
    queue = ['A', 'B', 'C']
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] === เริ่มระบบจำลองตู้กาแฟแบบ Multi-Thread ===")
    start_time = time()
    start_cpu = process_time() # บันทึกเวลาเริ่มต้นของ CPU

    threads = []
    # วนลูปสร้างเธรดสำหรับลูกค้าแต่ละคนในคิว
    for customer in queue:
        # กำหนดชื่อให้เธรด (name=) เพื่อให้ง่ายต่อการตรวจสอบและดู Log ตอนรันโปรแกรม
        t = threading.Thread(target=make_coffee, args=(customer,), name=f"Thread-{customer}")
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    duration = time() - start_time
    cpu_duration = process_time() - start_cpu

    # เรียกใช้ไลบรารี psutil เพื่อตรวจสอบการใช้หน่วยความจำ (RAM)
    process = psutil.Process(os.getpid())
    mem_mb = process.memory_info().rss / (1024 * 1024)

    print(f"[สรุปผล Multi-Thread]")
    print(f"เวลาที่ใช้จริง (Wall Time): {duration:0.2f} วินาที")
    print(f"เวลาที่ CPU ใช้ประมวลผลจริง (CPU Time): {cpu_duration:0.4f} วินาที")
    print(f"ทรัพยากร Memory (RAM) ที่ใช้: {mem_mb:.2f} MB")

if __name__ == "__main__":
    main()