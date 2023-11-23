#!/usr/bin/env python3

import sys

inp = sys.stdin.readlines()
nums = [int(n) for n in inp]

def replacer(num, modu):
    r = range(1, num + 1)
    rang = list(r)
    rang = [0 if n % modu != 0 else n for n in rang]
    return rang

for num in nums:
    print(f"Non-multiples of 3 replaced: {replacer(num, 3)}")
