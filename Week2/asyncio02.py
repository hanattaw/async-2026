# Program 2: The Coroutine Object
# Concept: Seeing that calling an async def function creates an "Object" but does not execute it yet.
import asyncio

async def greet():
    return "Hello"

coro_object = greet()  # Calling the async function creates a coroutine object

print(type(coro_object))  # This will show that it's a coroutine object

coro_object.close()  # Closing the coroutine object to free up resources