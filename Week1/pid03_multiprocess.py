from time import sleep, ctime, time
import multiprocessing
import threading
import os

# # ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คน
def make_coffee(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"{ctime()}| [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] กำลังชงกาแฟให้ ลูกค้า {customer_name}..." )
    sleep(5) #บล็อกการทำงานของ thread นี้ไว้ 5 วินาที
    print(f"{ctime()}| [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] ลูกค้า {customer_name} ได้รับกาแฟแล้ว!" )
    pass

def main():
    # คิวลูกค้า
    queue = {'A','B','C'}
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] === เริ่มระบบจำลองตู้กาแฟแบบ Multi-processing ===")
    start_time = time()

    processes = []
    # ลูปทำงานตามลำดับคิวเดียว (ทีละคน)
    for customer in queue:
        #สร้าง process ใหม่แยกจากกันเด็ดขาด
        p = multiprocessing.Process(target=make_coffee, args=(customer,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()

    duration = time() - start_time
    print(f"{ctime()} | ใช้เวลารวมทั้งหมด: {duration:.2f} วินาที")

    pass

# สั่งให้โปรแกรมทำงาน
if __name__ == "__main__":
    main()
    