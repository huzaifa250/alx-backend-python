#!/usr/bin/env python3
""" module to loop 10 times """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generates a sequence of 10 numbers. """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait 1 second
        yield random.randint(0, 10)  # Yield a random number between 0 and 10
