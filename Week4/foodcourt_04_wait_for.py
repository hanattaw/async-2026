# foodcourt_04_wait_for.py
import asyncio
import time
from time import ctime
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301025"
    print(f"{ctime()} | --- [Task 4] Practice using wait_for to handle timeouts ---")

    try:
        #
        print(f"{ctime()} | --- [System] Order Sent: ")
        results = await asyncio.wait_for(
            send_order_to_kitchen(MY_STUDENT_ID, "steak", "T-Bone Steak"),
            timeout=2.0
        )
        print(f"{ctime()} | System Response: {results}")

    except asyncio.TimeoutError:
        #
        print(f"{ctime()} | TimeoutError: The order took too long to complete.")




if __name__ == "__main__":
    asyncio.run(main())
