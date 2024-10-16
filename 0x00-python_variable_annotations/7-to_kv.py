#!/usr/bin/env python3
"""type-annotated function to_kv"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return tuple of parameters"""
    return (k, v ** 2)
