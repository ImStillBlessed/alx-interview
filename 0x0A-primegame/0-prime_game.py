#!/usr/bin/python3

def isWinner(x, nums):
    
    def SieveOfEratosthenes(n):
        result = []
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
            if (prime[p] == True):
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
        return 'Tie'
