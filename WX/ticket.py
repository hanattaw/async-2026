import sys

def calculate_ticket_price(age):
    if 7<= age < 13:
        price = 69
    elif 13 <= age < 60:
        price = 250
    elif age >= 60:
        price = 79
    else:
        price = "Invalid age"
    return price

def main():
    # เปลี่ยนมาเช็ก > 1 และใช้ sys.argv[-1] เพื่อความแม่นยำใน VPL
    if len(sys.argv) > 1:
        test_age = int(sys.argv[-1])
        result = calculate_ticket_price(test_age)
        print(result)
    else:
        test_age = 6
        result = calculate_ticket_price(test_age)
        print(f"Age: {test_age} -> Ticket Price: {result} Baht")

if __name__ == "__main__":
    main()