# Program 2: The Coroutine Object
# Concept: Seeing that calling an async def function creates an "Object" but does not execute it yet.
import asyncio

async def greet():
    print("Hello")


coro_object = greet()  # This creates a coroutine object but does not execute it yet.
print(type(coro_object))  # This will print <class 'coroutine'> indicating that it is a coroutine object.


coro_object.close()  # This will close the coroutine object, preventing it from being awaited or executed.
print(f"{coro_object}")  # This will print True, indicating that the coroutine object is closed.
coro_object.close()  # This will raise a RuntimeError because the coroutine object is already closed.