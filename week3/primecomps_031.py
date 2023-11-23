#!/usr/bin/env python3

import sys

inp = sys.stdin.readlines()
nums = [int(n) for n in inp]

def ifprime(num):
    i = 2
    if num == 1:
        return False
    while i < num // 2 + 1:
        if num % i == 0 and num != 2:
            return False
        i += 1
    return True

for n in nums:
    r = range(1, n + 1)
    rang = list(r)
    primes = [n for n in rang if ifprime(n)]
    print(f"Primes: {primes}")
