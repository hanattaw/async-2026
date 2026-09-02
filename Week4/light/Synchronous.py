import requests
import time

BASE_URL = "http://172.16.2.117:8088/api"
STUDENT_ID = "6710301027"

lights = [
    "light_1",
    "light_2",
    "light_3",
    "light_4"
]

start = time.perf_counter()

for light in lights:
    print(f"กำลังเปิด {light}...")
    response = requests.post(
        f"{BASE_URL}/{STUDENT_ID}/lights/{light}",
        json={"status": "ON"}
    )

    print(response.json())

end = time.perf_counter()

print("-" * 40)
print(f"ใช้เวลาทั้งหมด: {end - start:.2f} วินาที")