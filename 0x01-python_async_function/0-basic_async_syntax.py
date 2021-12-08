#!/usr/bin/env python3
"""
an asynchonous coroutine that takes in an integer argument
that waits for a random delay and eventually returns it
"""
import asyncio
import random


async def wait_random(max_dalay: int = 10) -> float:
    """waits for a rondom delay and eventually returns it"""
    max_delay = random.uniform(0, max_dalay)
    await asyncio.sleep(max_delay)
    max_delay = random.uniform(0, max_dalay)
    return max_delay
