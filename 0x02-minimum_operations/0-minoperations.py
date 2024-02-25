#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
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
