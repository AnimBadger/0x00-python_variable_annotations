#!/usr/bin/env python3
'''task 7 module'''
from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''function that takes a string and float and return a tuple'''
    return (k, float(v**2))
