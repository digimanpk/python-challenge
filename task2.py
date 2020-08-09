import asyncio
import time

printable_array = ["One", "Two", "Three", "Four"]


async def print_array(arr):
    index = 0
    for a in arr:
        await delayed_print(a, index)
        index += 1


async def delayed_print(printable, delay):
    await asyncio.sleep(2**delay)
    print(printable)

asyncio.run(print_array(printable_array))
