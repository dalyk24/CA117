#!/usr/bin/env python3

def factorial(n):
    if n == 0:
        return n + 1
    return n * factorial(n - 1)
