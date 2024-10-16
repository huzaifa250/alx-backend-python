#!/usr/bin/env python3
"""Module to defines an asynchronous function"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """return 10 random list number generated asynchronously"""
    res = [float(ise) async for ise in async_generator()]
    return res
    # Checking if the return value is annotated
    if 'return' in async_comprehension.__annotations__:
        print(f"The return type is annotated as: "
              f"{async_comprehension.__annotations__['return']}"
              )
    else:
        print("The return type is not annotated.")
