#!/usr/bin/env python3
"""Contains a function that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplies a float by multiplier"""
    return lambda numb: numb * multiplier
