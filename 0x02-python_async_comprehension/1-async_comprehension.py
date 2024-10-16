#!/usr/bin/env python3
""" Module to defines an asynchronous function"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    """return 10 random list number generated asynchronously"""
    return [ise async for ise in async_generator()]
