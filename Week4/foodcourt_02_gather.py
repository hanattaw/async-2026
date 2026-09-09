# foodcourt_02_gather.py
import asyncio
from time import ctime
from food_utils import send_order_to_kitchen

async def main(): 
    my_student_id = "6720301002"
    print(f"{ctime()} | --- [Task 2] Practice using gather to wait for all gruop orders ---")
    start_time = ctime()

    #1 spawn 3 concurrent tasks to order food from different kitchens
    t1 = asyncio.create_task(send_order_to_kitchen(my_student_id, "hainanese_chicken", "Chicken Rice"))
    t2 = asyncio.create_task(send_order_to_kitchen(my_student_id, "noodle", "Wonton Noodle"))
    t3 = asyncio.create_task(send_order_to_kitchen(my_student_id, "steak", "Sizzling Steak"))

    #2 use asyncio.gather to wait for all dishes to be prepared concurrently.
    result = await asyncio.gather(t1, t2, t3)
    for dish in result:
        print(f"{ctime()} | System Response: {dish}")
    

if __name__ == "__main__":
    asyncio.run(main())