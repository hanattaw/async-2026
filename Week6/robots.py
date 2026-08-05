import asyncio
import time
import httpx

# ==========================================
# 1. Configuration & Constants
# ==========================================
STUDENT_ID = "6710301017" 
BASE_URL = "http://172.16.2.117:8088"

# กำหนดลำดับชิ้นส่วนและหุ่นยนต์
PARTS = ["A", "B", "C"]
ROBOTS = ["robot_1", "robot_2", "robot_3", "robot_4"]

# ==========================================
# 2. Async Functions Development
# ==========================================

async def reset_factory(client: httpx.AsyncClient):
    async with client.post(f"/student/{STUDENT_ID}/reset") as response:
        if response.status_code == 200:
            print("Factory reset successful.")
        else:
            print(f"Factory reset failed with status code: {response.status_code}")
    
async def grab_part(client: httpx.AsyncClient, robot_id: str, part: str):
    async with client.post(f"/student/{STUDENT_ID}/robot/{robot_id}/grab", json={"part": part}) as response:
        if response.status_code == 200:
            print(f"{robot_id} successfully grabbed part {part}.")
        else:
            print(f"{robot_id} failed to grab part {part} with status code: {response.status_code}")

    

async def run_robot_task(client: httpx.AsyncClient, robot_id: str):


    """สั่งให้หุ่นยนต์ 1 ตัว ทำการหยิบชิ้นส่วน A, B, และ C ตามลำดับ"""
    # TODO: วนลูปหยิบชิ้นส่วนใน PARTS ตามลำดับเรียงกัน (Sequential inside single robot)
    for part in PARTS:
        await grab_part(client, robot_id, part)

    return f"{robot_id} completed all part grabs."

async def main():
    """ฟังก์ชันหลักสำหรับเริ่มการทำงานของหุ่นยนต์ทั้ง 4 ตัวแบบ Async"""
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=10.0) as client:
        print("Resetting Factory...")
        await reset_factory(client)
        
        start_time = time.time()
        print("Starting Async Robot Operation...")

        await asyncio.gather(
            *(run_robot_task(client, robot_id) for robot_id in ROBOTS)
        )
        
        elapsed_time = time.time() - start_time
        print(f"Finished all tasks in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())