#!/usr/bin/env python3
"""coroutine called async_generator that takes no arguments"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """coroutine will loop 10 times, each time asynchronously wait 1 second"""
    for _ in range(10):
        numb = uniform(0, 10)
        yield numb
        await asyncio.sleep(1)
