import asyncio
import httpx

# 1. แก้ไข IP และ Port ให้ตรงกับเครื่อง Server
SERVER_IP = "172.20.56.245" 
PORT = "8000"
SERVER_URL = f"http://{SERVER_IP}:{PORT}"

MY_STUDENT_ID = "6710301027"

async def hunt_coupons():
    async with httpx.AsyncClient() as client:
        print(f'[{MY_STUDENT_ID}] เริ่มต้นภารกิจล่าคูปอง...')

        # ยิงขอคูปองต่อเนื่อง 5 ครั้ง
        for attempt in range(1, 6):
            try:
                res = await client.post(
                    f"{SERVER_URL}/claim",
                    json={"student_id": MY_STUDENT_ID},
                    timeout=5.0
                )
                data = res.json()
                status = data.get("status")

                # ปรับให้ดึงคีย์ 'coupon' ตามที่ Server ส่งกลับมา
                print(f" - ครั้งที่ {attempt}: {status} -> {data.get('message', data.get('coupon'))}")

                # หากได้ครบ 2 ใบหรือหมดคูปองแล้ว ให้หยุดยิงทันที
                if status in ["LIMIT_REACHED", "OUT_OF_COUPONS"]:
                    break

            except Exception as e:
                print(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")
            
            # พักก่อนยิงรอบต่อไปเล็กน้อย
            await asyncio.sleep(0.02)
        
        # สรุปผลการล่าคูปอง
        print("\nกำลังสรุปการดึงคูปองของตนเอง...")
        try:
            res = await client.get(f"{SERVER_URL}/my-coupons/{MY_STUDENT_ID}")
            if res.status_code == 200:
                sammary = res.json()
                total = sammary.get("total_claimed", 0)
                coupon = sammary.get("claimed_coupons", [])
                print(f"สรุปผล [{MY_STUDENT_ID}]: ได้รับคูปองรวม {total} ใบ -> {coupon}")
            else:
                print(f"ดึงข้อมูลส่วนตัวไม่สำเร็จ Status Code: {res.status_code}")
        except Exception as e: # แก้ไขให้รองรับตัวแปร e 
            print(f"เกิดข้อผิดพลาดในการดึงข้อมูลส่วนตัว: {e}")

        # 2. ค้นหาข้อมูลสรุปทั้งหมด (/summary)
        print("\nกำลังค้นหาข้อมูลสรุปจาก Server (/summary)...")

        try:
            # 3. เปลี่ยนจาก BASE_URL เป็น SERVER_URL เพื่อแก้ Error
            res = await client.get(f"{SERVER_URL}/summary")

            if res.status_code == 200:
                summary_all = res.json()
                result = summary_all.get("completion_stats", "N/A")
                claims = summary_all.get("student_claims", {})

                print(f"\nข้อมูลจาก Server (รวมทั้งหมด):")
                print(f"completion_stats: {result}")

                for sid, coupons in claims.items():
                    print(f"- {sid}: {len(coupons)} รายการ ({coupons})")
            else:
                print(f"ไม่สามารถดึงข้อมูลได้: Status Code {res.status_code}")

        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการดึงข้อมูล: {e}")

if __name__ == "__main__":
    asyncio.run(hunt_coupons())