#!/usr/bin//env python3
'''task 6 module'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''function that take a list of int and float, and return sum'''
    return float(sum(mxd_lst))
