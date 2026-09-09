import requests
import time

BASE_URL = "http://172.16.2.117:8088"
STUDENT_ID = "6720301002"
LIGHT_IDS = ["light_1", "light_2", "light_3", "light_4"]


def get_lights_status():
    r = requests.get(f"{BASE_URL}/api/{STUDENT_ID}/lights")
    r.raise_for_status()
    return r.json()


def control_light_sync(light_id: str, status: str):
    """ควบคุมไฟ 1 ดวง แบบ sync — บล็อกรอจนกว่า hardware delay จะจบ"""
    url = f"{BASE_URL}/api/{STUDENT_ID}/lights/{light_id}"
    payload = {"status": status}
    t0 = time.time()
    r = requests.post(url, json=payload)
    elapsed = time.time() - t0
    r.raise_for_status()
    return r.json(), elapsed


def turn_on_all_sync():
    """เปิดไฟทุกดวงทีละดวง (sequential) — รอทีละตัว"""
    print("=== [SYNC] เปิดไฟทุกดวงทีละดวง ===")
    start = time.time()
    for light_id in LIGHT_IDS:
        data, elapsed = control_light_sync(light_id, "ON")
        print(f"  {light_id}: {data}  (ใช้เวลา {elapsed:.2f}s)")
    total = time.time() - start
    print(f"เวลารวมทั้งหมด: {total:.2f}s\n")
    return total


def reset_all_sync():
    """เรียก reset endpoint (server จัดการ logic ภายในเอง)"""
    print("=== [SYNC] Reset ไฟทั้งหมด ===")
    start = time.time()
    r = requests.delete(f"{BASE_URL}/api/{STUDENT_ID}/lights/reset")
    r.raise_for_status()
    elapsed = time.time() - start
    print(f"  response: {r.json()}  (ใช้เวลา {elapsed:.2f}s)\n")
    return elapsed


if __name__ == "__main__":
    print("สถานะก่อนเริ่ม:", get_lights_status())
    reset_all_sync()
    turn_on_all_sync()
    print("สถานะหลังทำ:", get_lights_status())