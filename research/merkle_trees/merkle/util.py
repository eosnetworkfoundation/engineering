#!/usr/bin/env python3

from typing import Annotated, Any, Optional, cast
# See https://github.com/annotated-types/annotated-types
from annotated_types import Gt, Ge, Interval
from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum

NonnegativeInt = Annotated[int, Ge(0)]
PositiveInt = Annotated[int, Gt(0)]
Bit = Annotated[int, Interval(ge=0, le=1)]

def powers_of_2(max: NonnegativeInt):
    """Generator that yields positive powers of 2 that are less than or equal to specified max value."""

    accumulator = 1
    while accumulator <= max:
        yield accumulator
        accumulator <<= 1


@dataclass
class NaturalRange:
    floor: NonnegativeInt
    ceil: NonnegativeInt  # must be >= floor


def log2(n: PositiveInt) -> NaturalRange:
    """
    Returns: (floor(log2(n)), ceil(log2(n))) where both members of pair are non-negative integer (assuming preconditions are met)

    Precondition: n > 0
    """

    floor_count = -1
    ceil_count = 0
    for i in powers_of_2(n):
        floor_count += 1
        if i != n:
            ceil_count += 1

    return NaturalRange(floor=floor_count, ceil=ceil_count)