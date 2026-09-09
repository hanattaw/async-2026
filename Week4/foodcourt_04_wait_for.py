# foodcourt_04_wait_for.py
import asyncio
from time import ctime, time
from food_utils import send_order_to_kitchen

async def main():
    my_student_id = "6720301002"
    print(f"{ctime()} | --- [Task 4] Practice using wait_for to handle timeouts ---")
    start_time = time()

    try:
        print(f"{ctime()} | [System] Order sent. Monitoring 2.0s timeout limit...")
        result = await asyncio.wait_for(
            send_order_to_kitchen(my_student_id, "steak", "T-one Steak"), 
            timeout=2.0
        )
        print(f"{ctime()} | Success: {result}")

    except asyncio.TimeoutError:
        print(f"{ctime()} | Timeout occurred: Steak took too long! Leaving the food court now. ")

if __name__ == "__main__":
    asyncio.run(main())