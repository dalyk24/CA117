#!/usr/bin/env python3

import sys

nums = sys.stdin.readlines()
inums = [int(num) for num in nums]

def multiples(num, multi):
    r = range(1, num + 1)
    rang = list(r)
    multis = [n for n in rang if n % multi == 0]
    return multis

for num in inums:
    multi3 = multiples(num, 3)
    multi4 = multiples(num, 4)
    print(f"Multiples of 3: {multi3}")
    print(f"Multiples of 3 squared: {[n**2 for n in multi3]}")
    print(f"Multiples of 4 doubled: {[n*2 for n in multi4]}")
    for n in multi3:
        if n not in multi4:
            multi4.append(n)
    multi4.sort()
    print(f"Multiples of 3 or 4: {multi4}")
    print(f"Multiples of 3 and 4: {[n for n in multi3 if n % 4 == 0]}")
