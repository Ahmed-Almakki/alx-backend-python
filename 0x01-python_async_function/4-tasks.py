#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""
import asyncio
from random import uniform
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    res = []
    for cmpltd in asyncio.as_completed(tasks):
        re = await cmpltd
        res.append(re)
    return res
