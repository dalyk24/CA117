#!/usr/bin/env python3

def collatz(n):
    if n <= 1:
        print(n)
        return n
    if n % 2 == 0:
        print(n)
        return collatz(n // 2)
    elif n % 2 == 1:
        print(n)
        return collatz(n * 3 + 1)
