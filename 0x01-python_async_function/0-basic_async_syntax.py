#!/usr/bin/env python3
"""
an asynchonous coroutine that takes in an integer argument
that waits for a random delay and eventually returns it
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a rondom delay and eventually returns it"""
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
