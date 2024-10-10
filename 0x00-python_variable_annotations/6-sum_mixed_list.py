#!/usr/bin/env python3
"""
Contains a function that takes a mixed list of integers and
floats and returns the sum of all the numbers in the list as float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """mixed list of integers & floats, returns
    sum of all the numbers in the list as float """
    return float(sum(mxd_lst))
