# Program 1: The First Coroutine Function
# Concept: Understanding async def and how it differs from a normal function.
import asyncio

#A regular function that returns a string


async def greet():
    return "Hello from  coroutine!"



print(type(greet))