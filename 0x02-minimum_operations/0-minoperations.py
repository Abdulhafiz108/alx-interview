#!/usr/bin/python3
"""
This file contains function minOperations(n)
"""
from sympy import primefactors


def minOperations(n) -> int:
    """
    This function returns the fewest number of operations needed to
    result in exactly n H characters in the file.
    """
    if (n == 0) or (n == 1):
        return n

    number = n
    factors = []
    while number > 1:
        factors.append(primefactors(number)[0])
        number = number / primefactors(number)[0]

    return sum(factors)
