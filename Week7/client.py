import asyncio
import httpx

# เปลี่ยน IP ตรงนี้ให้เป็น IP เครื่องที่เป็น Server (เช่น "192.168.1.50")
SERVER_IP = "172.20.56.245"
PORT = 8000
SERVER_URL = f"http://{SERVER_IP}:{PORT}"

# ระบุรหัส/ชื่อนักเรียนของผู้ส่ง
MY_STUDENT_ID = "6720301002"


async def hunt_coupons():
    async with httpx.AsyncClient() as client:
        print(f"[{MY_STUDENT_ID}] เริ่มต้นภารกิจล่าคูปอง...")

        # -------------------------------------------------
        # 0. ยิงขอคูปองแบบต่อเนื่อง พยายามจนกว่าจะได้ครบ 2 ใบ
        # -------------------------------------------------
        for attempt in range(1, 6):
            try:
                res = await client.post(
                    f"{SERVER_URL}/claim",
                    json={"student_id": MY_STUDENT_ID},
                    timeout=5.0
                )
                data = res.json()
                status = data.get("status")

                if status == "SUCCESS":
                    print(f"  -- ครั้งที่ {attempt}: [{status}] ได้คูปอง {data.get('coupon')} "
                          f"(รวมตอนนี้ {data.get('total_owned')} ใบ)")
                else:
                    print(f"  -- ครั้งที่ {attempt}: [{status}] -> {data.get('message')}")

                # หากได้ครบ 2 ใบ หรือของหมดแล้ว ให้หยุดการยิงต่อ
                if status in ["LIMIT_REACHED", "OUT_OF_COUPONS"]:
                    break

            except Exception as e:
                print(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")

            # พักก่อนจะยิงรอบถัดไปเล็กน้อย
            await asyncio.sleep(0.02)

        # -------------------------------------------------
        # 1. เรียกดูภาพรวมทั้งหมดจาก Server (/summary)
        #    (server นี้ไม่มี endpoint /my-coupons แยก จึงดึงข้อมูลของตนเอง
        #     มาจาก student_claims ใน /summary แทน)
        # -------------------------------------------------
        print("\nกำลังเรียกดูภาพรวมทั้งหมดจาก Server (/summary)...")
        my_total = 0
        my_coupons = []
        try:
            res = await client.get(f"{SERVER_URL}/summary")
            if res.status_code == 200:
                summary_all = res.json()
                rem_coupons = summary_all.get("remaining_coupons", "N/A")
                claims = summary_all.get("student_claims", {})

                print(f"จำนวนคูปองคงเหลือใน Server: {rem_coupons} ใบ")
                print("รายการคูปองที่แจกจ่ายไปแล้ว:")
                for sid, coupons in claims.items():
                    print(f"  - {sid}: ได้ไป {len(coupons)} ใบ -> {coupons}")

                my_coupons = claims.get(MY_STUDENT_ID, [])
                my_total = len(my_coupons)
            else:
                print(f"ไม่สามารถตรวจสอบภาพรวมได้ Status Code: {res.status_code}")
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการตรวจสอบภาพรวม: {e}")

        # -------------------------------------------------
        # 2. ยืนยันผลลัพธ์ (ต้องได้คูปองครบ 2 ใบ) — เช็คจากข้อมูลจริงที่ดึงมาใน Step 1
        # -------------------------------------------------
        print("\n" + "=" * 40)
        if my_total == 2:
            print(f" ผ่าน: [{MY_STUDENT_ID}] ได้คูปองครบ 2 ใบ -> {my_coupons}")
        elif my_total == 1:
            print(f" ยังไม่ครบ: [{MY_STUDENT_ID}] ได้คูปองเพียง 1 ใบ -> {my_coupons}")
        else:
            print(f" ไม่ผ่าน: [{MY_STUDENT_ID}] ยังไม่ได้คูปองเลย")
        print("=" * 40)


if __name__ == "__main__":
    asyncio.run(hunt_coupons())