#!/usr/bin/env python3

import sys

digit = sys.stdin.read().strip()

while len(digit) > 1:
    curr = 1
    for char in digit:
        if char != "0":
            curr *= int(char)
    digit = str(curr)

print(digit)
