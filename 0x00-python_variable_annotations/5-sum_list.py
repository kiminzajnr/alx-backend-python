#!/usr/bin/env python3
"""
Complex types - list of floats
"""


def sum_list(input_list: list) -> float:
    """return sum of list floats"""
    sum_ = 0
    for val in input_list:
        sum_ += val
    # could be sum(input_list)
    return sum_
