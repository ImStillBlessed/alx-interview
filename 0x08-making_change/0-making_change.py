#!/usr/bin/python3
"""
The coin change algorithm is a dynamic programming problem
that involves finding the minimum number of coins required
to make a certain amount of change. The problem can be
solved using a bottom-up approach, where we build a table
of the minimum number of coins required to make change for
each amount from 0 to the target amount.
"""


def makeChange(coins, total):
    """
    The makeChange function takes a list of coin values and a
    args:
        coins: list of coin values
        total: the target amount of change
    return:
        the minimum number of coins required to make the change
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
