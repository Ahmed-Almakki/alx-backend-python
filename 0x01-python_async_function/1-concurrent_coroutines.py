#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""
import asyncio
from random import uniform
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays"""
    pr = []
    for i in range(n):
        pr.append(asyncio.create_task(wait_random(max_delay)))
    return [await task for task in pr]
