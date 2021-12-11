#!/usr/bin/env python3
"""
a coroutine that takes no arguments using async generator
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """loop 10 times with 1 sec wait then yield a random number"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
