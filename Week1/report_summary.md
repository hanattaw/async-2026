สรุปผลการทดลอง Coffee Machine Concurrency (Week1)

สคริปต์ที่รัน:
- `coffee01_synchronous.py` — Synchronous (ทีละคน)
- `coffee02_thread.py` — Multi-thread (threads)
- `coffee03_multiprocess.py` — Multi-process (processes)
- `coffee04_asyncio.py` — Asyncio (event loop)
- `ps01_synchronous.py`, `ps02_thread.py`, `ps03_multiprocess.py`, `ps04_asyncio.py` — เวอร์ชันวัด resource
- `up01_synchronous.py`, `up02_thread.py`, `up03_multiprocess.py`, `up04_asyncio.py` — เวอร์ชันแยกหน้าจออัปเดต (Update)

คำสั่งทดลอง (เรียกจากโฟลเดอร์โปรเจคหลัก):
```powershell
& .\.venv\Scripts\Activate.ps1 ; python .\async-2026\Week1\coffee01_synchronous.py
& .\.venv\Scripts\Activate.ps1 ; python .\async-2026\Week1\coffee02_thread.py
& .\.venv\Scripts\Activate.ps1 ; python .\async-2026\Week1\coffee03_multiprocess.py
& .\.venv\Scripts\Activate.ps1 ; python .\async-2026\Week1\coffee04_asyncio.py
& .\.venv\Scripts\Activate.ps1 ; python .\async-2026\Week1\ps01_synchronous.py
& .\.venv\Scripts\Activate.ps1 ; python .\async-2026\Week1\ps02_thread.py
& .\.venv\Scripts\Activate.ps1 ; python .\async-2026\Week1\ps03_multiprocess.py
& .\.venv\Scripts\Activate.ps1 ; python .\async-2026\Week1\ps04_asyncio.py
& .\.venv\Scripts\Activate.ps1 ; python .\async-2026\Week1\up01_synchronous.py
& .\.venv\Scripts\Activate.ps1 ; python .\async-2026\Week1\up02_thread.py
& .\.venv\Scripts\Activate.ps1 ; python .\async-2026\Week1\up03_multiprocess.py
& .\.venv\Scripts\Activate.ps1 ; python .\async-2026\Week1\up04_asyncio.py
```

ผลลัพธ์ (ที่จับได้จากการรันจริงบนเครื่องนี้):
- `coffee01_synchronous.py` → Wall Time: 15.00 วินาที
  - ทำงานทีละคน (A → B → C) แต่ละคนใช้ 5 วินาที (ชง 5s)
- `coffee02_thread.py` → Wall Time: 5.39 วินาที
  - งานทำพร้อมกันบนหลาย thread (แต่ยังแชร์ process เดียว)
- `coffee03_multiprocess.py` → Wall Time: 5.01 วินาที
  - แต่ละ process ทำงานแยกตัว (เวลาใกล้เคียง multi-thread ในกรณีนี้)
- `coffee04_asyncio.py` → Wall Time: 2.02 วินาที
  - ใช้การสลับงานแบบ non-blocking (`await asyncio.sleep`) ทำให้งาน I/O-like ทำพร้อมกันได้จริง

- `ps01_synchronous.py` → Wall Time: 6.00 วินาที, CPU Time: 0.0000s, Memory: 17.74 MB
- `ps02_thread.py` → Wall Time: 2.00 วินาที, CPU Time: 0.0156s, Memory: 18.09 MB
- `ps03_multiprocess.py` → Wall Time: 2.12 วินาที, CPU Time: 0.0000s, Total Memory (main+children): 81.46 MB
- `ps04_asyncio.py` → Wall Time: 2.00 วินาที, CPU Time: 0.0000s, Memory: 24.89 MB

- `up01_synchronous.py` → Total time: 6.00 วินาที (ทำทีละคน ทำให้รวม 3*2s)
- `up02_thread.py` → Total time: 2.00 วินาที (ทำพร้อมกันบน threads)
- `up03_multiprocess.py` → Total time: 2.08 วินาที (ทำพร้อมกันบน processes)
- `up04_asyncio.py` → Total time: 2.00 วินาที (ทำพร้อมกันด้วย asyncio)

ข้อสังเกตและคำอธิบายสั้น ๆ:
- โจทย์กำหนดว่าแต่ละลูกค้าต้องทำ 2 งานต่อเนื่อง: `Make Coffee` = 1.0s, `Update LCD Screen` = 1.0s → รวม 2.0s ต่อคน ถ้าทำทีละคนจะได้ ~6s
- ในการทดลองบนเครื่องนี้:
  - `coffee01` (original) ใช้เวลารวม 15s เพราะตัวต้นฉบับใช้ sleep 5s ต่อขั้นตอน (ตัวอย่างเดิมใน repo)
  - เวอร์ชัน `ps*` และ `up*` ที่ผมสร้างใหม่ใช้ 1s ต่อขั้นตอน ทำให้ผลตามคาดเมื่อเปรียบเทียบสถาปัตยกรรม
  - Thread/Process/Asyncio ทำให้ wall time ลดลงอย่างมากเมื่อเทียบกับ synchronous
- Memory/CPU:
  - `ps03_multiprocess.py` แสดงค่า memory สูงสุดเพราะ spawn processes (แต่ละ process มี RSS ของตัวเอง)
  - `ps02_thread.py` และ `ps04_asyncio.py` ใช้หน่วยความจำน้อยกว่า (single process)
  - CPU Time ที่วัดได้ต่ำเพราะงานหลักเป็น sleep (I/O-like)

ไฟล์ที่แก้ไข/รันแล้ว:
- `async-2026/Week1/coffee04_asyncio.py` (แก้ข้อความ และรัน)
- `async-2026/Week1/ps01_synchronous.py`, `ps02_thread.py`, `ps03_multiprocess.py`, `ps04_asyncio.py` (เพิ่มการวัด resource)
- `async-2026/Week1/up01_synchronous.py`, `up02_thread.py`, `up03_multiprocess.py`, `up04_asyncio.py` (เพิ่มเวอร์ชันอัปเดตหน้าจอ)

ถัดไปที่ผมทำให้ได้:
- สร้างสไลด์สรุป (PowerPoint/PDF) ตามตัวอย่างที่คุณแนบ
- หรือ สร้างไฟล์ ZIP พร้อมสำหรับส่งงาน

บอกว่าต้องการอย่างไหน ผมจัดให้ได้เลยครับ.