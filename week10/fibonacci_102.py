#!/usr/bin/env python3

def fibonacci(n):
    if n == 0:
        return n + 1
    elif n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
