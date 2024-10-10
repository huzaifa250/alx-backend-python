#!/usr/bin/env python3
"""Module contains a function that sums a list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Computes the sum list of float numbers """
    if input_list is None:
        return 0
    else:
        return float(sum(input_list))
