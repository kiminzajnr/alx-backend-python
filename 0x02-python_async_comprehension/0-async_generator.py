#!/usr/bin/env python3
"""
a coroutine that takes no arguments using async generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """loop 10 times with 1 sec wait then yield a random number"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
