from time import sleep, ctime, time

def update_cup_number(customer_name):
    print(f"{ctime()}| LCD: Processing for customer {customer_name}..." )
    sleep(1) #บล็อกการทำงานของ LCD นี้ไว้ 1 วินาที
    print(f"{ctime()}| LCD: Done for customer {customer_name}." )
    pass

def make_coffee(customer_name):

    print(f"{ctime()}| Making coffee for {customer_name}..." )
    sleep(1) #บล็อกการทำงานของ thread นี้ไว้ 1 วินาที
    print(f"{ctime()}| Coffee ready for {customer_name}!" )
    
    pass

def main():
    # คิวลูกค้า
    queue = {'A','B','C'}

    print(f"{ctime()} | === Synchronous Coffee Machine ===")
    start_time = time()

    # ลูปทำงานตามลำดับคิวเดียว (ทีละคน)
    for customer in queue:
        make_coffee(customer)
        update_cup_number(customer)

    duration = time() - start_time
    print(f"{ctime()} | Total time: {duration:.2f} Seconds")
    pass

if __name__ == "__main__":
    main()