from time import sleep, ctime, time
import os
import threading
import random

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คนแบบซิงโครนัส
def make_coffee(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] กำลังชงกาแฟให้ลูกค้า {customer_name}...")
    random_sleep = random.uniform(3, 5)
    sleep(random_sleep) # บล็อกการทำงานของ Thread นี้ไว้ 5 วินาทีเต็ม
    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Thread Name: {thread_name}] ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")

def main():
    queue = ['A', 'B', 'C']
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] เริ่มต้นการทำงานของร้านกาแฟ...")
    start_time = time()

    threads = []
    #ลูปการทำงาน Thread
    for customer in queue:
        t = threading.Thread(target=make_coffee, args=(customer,), name=f"CoffeeThread-{customer}")
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    duration = time() - start_time
    print(f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] ร้านกาแฟปิดทำการแล้ว! ใช้เวลาในการทำงานทั้งหมด: {duration:.2f} วินาที") 

if __name__ == "__main__":
    start_time = time()
    main()        