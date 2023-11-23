#!/usr/bin/env python3

import sys

for s in sys.stdin.readlines():
    orders = [int(t) for t in s.strip().split()]
    sorders = sorted(orders, reverse = True)
    print(sum(sorders) - sum(sorders[2::3]))
