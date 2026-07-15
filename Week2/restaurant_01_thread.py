from time import sleep, ctime, time
import threading

# 1. ขั้นตอนต้อนรับเริ่มพร้อมกันทั้งหมด ทำแบบ Synchronous เร็วที่สุด
def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")

# 2. กระบวนการส่วนตัวของลูกค้าแต่ละคน ที่จะถูกนำไปรันแยกใน Thread ต่าง ๆ
def customer_private_workflow(customer):

    # Take Order
    print(f"{ctime()} [Thread-{customer}] Taking Order ...")
    sleep(1)
    print(f"{ctime()} [Thread-{customer}] Taking Order ...Done!")

    # Do Cooking
    print(f"{ctime()} [Thread-{customer}] Cooking Spaghetti ...")
    sleep(1)
    print(f"{ctime()} [Thread-{customer}] Cooking Spaghetti ...Done!")

    # Manage Bar
    print(f"{ctime()} [Thread-{customer}] Manage Bar for Drinks ...")
    sleep(1)
    print(f"{ctime()} [Thread-{customer}] Manage Bar for Drinks ...Done!")

    print(f"{ctime()} [Thread-{customer}] All served!\n")


if __name__ == "__main__":
    customers = ['A', 'B', 'C']
    start_time = time()

    # ------------------------------------------------------------
    # PHASE 1: Greet ลูกค้าทั้งหมดแบบ Synchronous (เข้าเรียงคิวตามชื่อ)
    # ------------------------------------------------------------
    for customer in customers:
        greet_diners(customer)

    print(f"\n{ctime()} ---- All customers greeted. Splitting into individual threads ----\n")

    # ------------------------------------------------------------
    # PHASE 2: แยกลูกค้าให้แต่ละคนไปทำกระบวนการที่เหลือพร้อมกัน
    # ------------------------------------------------------------
    customer_threads = []

    for customer in customers:
        # สร้าง Thread ใหม่สำหรับลูกค้าแต่ละคน
        # แล้วกำหนดให้เริ่มทำงานที่ customer_private_workflow()
        t = threading.Thread(
            target=customer_private_workflow,
            args=(customer,)
        )

        customer_threads.append(t)
        t.start()     # สั่งให้ Thread เริ่มทำงานทันที

    # รอให้ทุก Thread ทำงานเสร็จ
    for t in customer_threads:
        t.join()

    duration = time() - start_time

    print(f"\n{ctime()} Finished Entire Restaurant Operation in {duration:.2f} seconds.")