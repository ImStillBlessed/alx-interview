#!/usr/bin/python3
"""Game module for interview"""


def sieve_of_eratosthenes(max_num):
    """ Returns a list of primes up to max_num using Sieve of Eratosthenes."""
    is_prime = [True] * (max_num + 1)
    p = 2
    while (p * p <= max_num):
        if (is_prime[p]):
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = []
    for p in range(2, max_num + 1):
        if is_prime[p]:
            prime_numbers.append(p)
    return prime_numbers


def isWinner(x, nums):
    """Determines the winner of each game, given a list of integers."""
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n <= 1:
            continue

        current_set = list(range(1, n + 1))
        current_turn = 0  # 0 for Maria, 1 for Ben

        while True:
            if current_turn == 0:  # Maria's turn
                can_move = False
                for prime in primes:
                    if prime > n:
                        break
                    if prime in current_set:
                        can_move = True
                        current_set = [num for num in
                                       current_set if num % prime != 0]
                        break
                if not can_move:
                    ben_wins += 1
                    break
                current_turn = 1

            else:  # Ben's turn
                can_move = False
                for prime in primes:
                    if prime > n:
                        break
                    if prime in current_set:
                        can_move = True
                        current_set = [num for num in
                                       current_set if num % prime != 0]
                        break
                if not can_move:
                    maria_wins += 1
                    break
                current_turn = 0

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
