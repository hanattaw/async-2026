# Program 2: The Coroutine Object
# Concept: Seeing that calling an async def function creates an "Object" but does not execute it yet.
import asyncio

async def greet():
    print("Hello")

corotine_object = greet()
print(type(corotine_object))

coro_object = greet()

print(f'Corotine object: {coro_object}')

coro_object.close()