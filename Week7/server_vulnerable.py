import asyncio
from typing import Dict, List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

STUDENTS = ["Student_01", "Student_02", "Student_03", "Student_04", "Student_05"]
GROUP_SIZE = len(STUDENTS)
TOTAL_COUPONS = (GROUP_SIZE * 2) - 1

coupons_db: List[str] = [f"COUPON-{i:02d}" for i in range(1, TOTAL_COUPONS + 1)]

#ใช้ Pointer ชีัตำแหน่งคูปองถัดไปที่จะแจก
current_coupon_index = 0

student_claims: Dict[str, List[str]] = {student: [] for student in STUDENTS}

class ClaimRequest(BaseModel):
    student_id: str

@app.post("/claim")
async def claim_coupon(req: ClaimRequest):
    global current_coupon_index
    student_id = req.student_id

    # ตรวจสอบว่าผู้ส่งเป็นนักเรียนที่อยู่ในกลุ่มหรือไม่
    if student_id not in STUDENTS:
        return {"status": "INVALID_STUDENT", "message": "ไม่พบรายชื่อในระบบ"}

    # ตรวจสอบว่าผู้ส่งได้คูปองครบ 2 ใบแล้วหรือยัง
    if len(student_claims[student_id]) >= 2:
        return {"status": "LIMIT_REACHED", "message": "คุณได้รับคูปองครบ 2 ใบแล้ว"}

    # Critical Section (ไม่มี Lock)
    if current_coupon_index < len(coupons_db):
       #1. อ่านค่า Index ปจจุบันมาเก็บไว้
        index_to_claim = current_coupon_index
        
        await asyncio.sleep(0.1)  # จำลองความล่าช้าในการประมวลผล
        #2. แจกคูปองให้ผู้ส่ง
        claimed_coupon = coupons_db[index_to_claim]
        student_claims[student_id].append(claimed_coupon)

        #3. ขยับ Index ไปใบถัดไป (ถ้ามี Request เข้ามาอีก จะได้แจกคูปองใบถัดไป)
        current_coupon_index = index_to_claim + 1

        return {"status": "SUCCESS", "claimed_coupon": claimed_coupon, "total_owned": len(student_claims[student_id])}

    return {"status": "OUT_OF_STOCK", "message": "คูปองหมดแล้ว"} 



@app.get("/summary")
async def get_summary():
    return {
        "remaining_stock": len(coupons_db) - current_coupon_index,
        "student_claims": student_claims
    }