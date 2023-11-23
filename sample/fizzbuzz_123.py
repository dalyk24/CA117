#!/usr/bin/env python3

import sys

nums = [int(n) for n in sys.stdin.readline().strip().split()]

for m in range(1, nums[2] + 1):
    if m % nums[0] == 0 and m % nums[1] == 0:
        print('fizzbuzz')
    elif m % nums[0] == 0:
        print('fizz')
    elif m % nums[1] == 0:
        print('buzz')
    else:
        print(m)
