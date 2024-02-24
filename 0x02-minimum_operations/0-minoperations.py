#!/usr/bin/env python3
"""This module contains function minOperations"""
from sympy import isprime


def minOperations(n) -> int:
    """
    This function returns the fewest number of operations needed to
    result in exactly n H characters in the file.
    """
    if (n == 0) or (n > 3 and isprime(n)):
        return 0

