#!/usr/bin/env python3
"""
execute multipe coroutines at the same time with async
"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with specified max_delay"""
    lst = []
    sorted_lst = []
    i = 0
    while i < n:
        spawn = await task_wait_random(max_delay)
        lst.append(spawn)
        i += 1
    y = 0
    while y < n:
        minimum = lst[0]
        for x in lst:
            if x < minimum:
                minimum = x
        sorted_lst.append(minimum)
        lst.remove(minimum)
        y += 1
    return sorted_lst
