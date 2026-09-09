# Program 10: Extracting Return Values from Tasks
# Concept: Accessing returned results from completed Task objects using .result() or direct assignment.
import asyncio
import time # เพิ่มการ import time สำหรับใช้ ctime()

# 1. สร้างคลาส Customer แบบง่ายๆ เพื่อให้มี attribute .name
class Customer:
    def __init__(self, name):
        self.name = name

async def calculate(customer, base_price):
    # แก้ไข ctime() เป็น time.ctime()
    print(f"{time.ctime()} Start calculating final price for {customer.name}!")
    await asyncio.sleep(1)  # Simulate calculation time
    final_price = base_price * 1.07  # Example calculation
    print(f"{time.ctime()} Finished calculating final price for {customer.name}!")
    return final_price

async def main():
    # 2. สร้างตัวแปร customer_a และ customer_b ก่อนนำไปใช้งาน
    customer_a = Customer("Alice")
    customer_b = Customer("Bob")

    task_a = asyncio.create_task(calculate(customer_a, 100))
    task_b = asyncio.create_task(calculate(customer_b, 200))

    result_a = await task_a  # Await the completion of task_a and get the result
    result_b = await task_b  # Await the completion of task_b and get the result

    # เพิ่มการแสดงชื่อลูกค้าให้ชัดเจนขึ้น (ทางเลือก)
    print(f"\nFinal price for {customer_a.name}: ${result_a:.2f}")
    print(f"Final price for {customer_b.name}: ${result_b:.2f}")
    print(f"Combined final price: ${result_a + result_b:.2f}")

if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine using the event loop