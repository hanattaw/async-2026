import asyncio

from light_utils import control_light, BASE_URL, reset_all_lights

STUDENT_ID = "6710301025"  
LIGHT_IDS = ["light_1", "light_2", "light_3", "light_4"]
async def async_turn_on_all(student_id: str = STUDENT_ID):
    print("== ปิดไฟพร้อมกันทั้งหมด (async) ==")

    # reset lights before running tasks
    await reset_all_lights(student_id)

if __name__ == "__main__":
    asyncio.run(async_turn_on_all())