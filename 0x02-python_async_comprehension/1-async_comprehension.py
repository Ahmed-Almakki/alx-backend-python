#!/usr/bin/env python3
"""Async Comprehensions"""
import asyncio
from random import uniform
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine well collect 10 random number
    Return:
        10 random number
    """
    return [i async for i in async_generator()]
