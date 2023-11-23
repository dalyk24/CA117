#!/usr/bin/env python3

def power(n, m):
    if m == 0:
        return m + 1
    return n * power(n, m - 1)



