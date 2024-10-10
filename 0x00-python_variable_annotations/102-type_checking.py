#!/usr/bin/env python3
from typing import Tuple, List
"""Module task 102"""


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """function attempts to create a zoomed-in version of a given
    tuple (or list) by repeating each element specified number of times"""

    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
