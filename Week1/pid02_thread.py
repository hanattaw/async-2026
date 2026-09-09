from time import sleep, ctime, time
import threading
import os

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คน
def make_coffee(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"[{ctime()}] Process ID: {pid}, Thread ID: {thread_id}, Thread Name: {thread_name} - กำลังทำกาแฟให้ลูกค้า {customer_name}...")
    sleep(5)  # จำลองเวลาที่ใช้ในการทำกาแฟ
    print(f"[{ctime()}] Process ID: {pid}, Thread ID: {thread_id}, Thread Name: {thread_name} - ทำกาแฟให้ลูกค้า {customer_name} เสร็จแล้ว!")

def main():
    queue = ["A", "B", "C"]
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id
    main_thread_name = threading.current_thread().name
    start_time = time()

    print(f"[{ctime()}] Main Process ID: {main_pid}, Main Thread ID: {main_tid} - เริ่มทำงานจำลองตู้กาแฟ...")
    start_time = time()

    for customer in queue:
        thread = threading.Thread(target=make_coffee, args=(customer,), name=f"CoffeeThread-{customer}")
        thread.start()

    for t in threading.enumerate():
        if t is not threading.current_thread():
            t.join()

    duration = time() - start_time
    print(f"[{ctime()}] Main Process ID: {main_pid}, Main Thread ID: {main_tid} - ทำงานเสร็จแล้ว! ใช้เวลาทั้งหมด: {duration:.2f} วินาที")

if __name__ == "__main__":
    main()