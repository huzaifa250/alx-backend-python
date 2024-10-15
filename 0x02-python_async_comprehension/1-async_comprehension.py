#!/usr/bin/env python3
""" Module to returns 10 random numbers using async comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    res = [ise async for ise in async_generator()]
    return res
