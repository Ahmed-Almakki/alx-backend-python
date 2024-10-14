#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay"""
    wait = uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
