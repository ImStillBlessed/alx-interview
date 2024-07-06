#!/usr/bin/python3
"""Game module for interview"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game between Ben and Maria.

    The game consists of multiple rounds.
    In each round, the number of primes
    less than or equal to a given number is counted.
    If the count is even, Ben
    scores a point. If the count is odd, Maria scores a point.
    The winner is the
    one with the most points after all rounds.

    Args:
        x (int): The number of rounds to be played.
        nums (List[int]): A list of integers
                representing the upper bounds for
                each round.

    Returns:
        str: 'Ben' if Ben wins, 'Maria' if Maria wins,
            'Tie' if both have the
            same score.

    Example:
        >>> isWinner(3, [4, 5, 1])
        'Ben'
    """

    def SieveOfEratosthenes(n):
        """
        Generate a list of prime numbers up
        to n (inclusive) using the Sieve of Eratosthenes algorithm.

        Args:
            n (int): The upper bound for generating prime numbers.

        Returns:
            List[int]: A list of prime numbers less than or equal to n.
        """
        result = []
        prime = [True for i in range(n+1)]
        p = 2
        while p * p <= n:
            if prime[p]:
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        for p in range(2, n+1):
            if prime[p]:
                result.append(p)
        return result

    ben = 0
    maria = 0
    for n in nums:
        primes = SieveOfEratosthenes(n)
        if len(primes) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return 'Ben'
    elif maria > ben:
        return 'Maria'
    else:
        return None
