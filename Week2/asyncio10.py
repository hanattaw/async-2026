# Program 10: Extracting Return Values from Tasks
# Concept: Accessing returned results from completed Task objects using .result() or direct assignment.
import asyncio

async def Calculate_bill(customer, base_price):
    print(f"Calculatting receipt for Customer {customer}")
    await asyncio.sleep(1)  # Simulate a delay in calculation
    final_price = base_price * 1.07  # Adding a 20% tax
    return final_price

async def main():
    task_a = asyncio.create_task(Calculate_bill("A", 100))
    task_b = asyncio.create_task(Calculate_bill("B", 200))

    result_a = await task_a  # Awaiting the first task and getting its result
    result_b = await task_b  # Awaiting the second task and getting its result

    print(f"\nfinal bill: ${result_a:.2f}")
    print(f"\n final bill: ${result_b:.2f}")  
    print(f"Combined Total bill: ${result_a + result_b:.2f}")

if __name__ == "__main__":
    asyncio.run(main())  # Run the coroutine object using the event loop
