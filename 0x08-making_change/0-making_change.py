#!/usr/bin/python3
"""
This module contains function makeChange
"""


def makeChange(coins, total):
    """
    This function determines the fewest number of coins
    needed to meet a given amount total
    """
    n_coins = 0
    if total <= 0:
        return n_coins
    coins.sort(reverse=True)
    while (total > 0 and coins):
        n = int(total / coins[0])
        total = total - (coins[0] * n)
        n_coins = n_coins + n
        coins.remove(coins[0])
    if total != 0:
        return -1
    return n_coins
