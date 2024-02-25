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
        factors.append(smallest_divisor(number))
        number = number // smallest_divisor(number)

    return sum(factors)

def smallest_divisor(n):
    """
    Find the smallest integer greater than 1 that divides n without remainder.
    """
    if n <= 1:
        return n

    for i in range(2, n+1):
        if n % i == 0:
            return i
