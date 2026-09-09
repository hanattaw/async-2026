import asyncio
import httpx

async def get_user_name(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url)
            return response.json()["name"]
    except httpx.ConnectError:
        # ถ้าหาที่อยู่เว็บไม่เจอ (เน็ตหลุด) ให้ส่งข้อความนี้กลับไปแทน โปรแกรมจะได้ไม่พัง
        return "ไม่สามารถเชื่อมต่ออินเทอร์เน็ตได้ (ConnectError)"
    except Exception as e:
        return f"เกิดข้อผิดพลาด: {e}"
    
async def main():
    name1, name2 = await asyncio.gather(get_user_name(1), get_user_name(2))
    print(f"User 1: {name1}, User 2: {name2}")

if __name__ == "__main__":
    asyncio.run(main())