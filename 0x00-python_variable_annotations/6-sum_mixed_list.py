#!/usr/bin/env python3
""" type-annotated function sum_mixed_list"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ return sum of mixd list"""
    return sum(mxd_lst)
