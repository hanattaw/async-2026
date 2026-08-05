import asyncio
import time
import httpx

STUDENT_ID = "6710301017" 
BASE_URL = "http://172.16.2.117:8088"

PARTS = ["A", "B", "C"]
ROBOTS = ["robot_1", "robot_2", "robot_3", "robot_4"]

async def reset_factory(client: httpx.AsyncClient):
    response = await client.post(f"/student/{STUDENT_ID}/reset") 
    
    if response.status_code == 200:
        print("Factory reset successful.")
    else:
        print(f"Factory reset failed with status code: {response.status_code}")
        
    return response.json()
    
async def grab_part(client: httpx.AsyncClient, robot_id: str, part: str):
    response = await client.post(
        f"/student/{STUDENT_ID}/robot/{robot_id}/grab", 
        json={"part": part}
    )
    
    if response.status_code == 200:
        print(f"{robot_id} successfully grabbed part {part}.")
    else:
        print(f"{robot_id} failed to grab part {part} with status code: {response.status_code}")
        
    return response.json()

async def run_robot_task(client: httpx.AsyncClient, robot_id: str):
    results = [] 
    
    for part in PARTS:
        res = await grab_part(client, robot_id, part)
        results.append(res)

    return results

async def main():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=10.0) as client:
        print("Resetting Factory...")
        await reset_factory(client)
        
        start_time = time.time()
        print("Starting Async Robot Operation...")

        tasks = [run_robot_task(client, robot_id) for robot_id in ROBOTS]
        all_results = await asyncio.gather(*tasks)
        
        elapsed_time = time.time() - start_time
        print(f"Finished all tasks in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())