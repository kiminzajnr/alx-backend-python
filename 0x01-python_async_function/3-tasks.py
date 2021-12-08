#!/usr/bin/env python3
"""
Creating tasks using asyncio
"""
import asyncio
from typing import Awaitable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable:
    """returns asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
