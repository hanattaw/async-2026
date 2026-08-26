# Program 2: The Coroutine Object
# Concept: Seeing that calling an async def function creates an "Object" but does not execute it yet.
import asyncio
from fileinput import close
async def greet():
    print("Hello!")

#calling the coroutine function does not execute it, but returns a coroutine object
coroutine_object = greet()

#notice that hello is not printed yet, because the coroutine has not been executed
print(type(coroutine_object))
#to prevent program from exiting before the coroutine is executed, we can use asyncio.run() to run the coroutine
coro_object = close()