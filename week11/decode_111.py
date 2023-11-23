#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin.readlines()]
vowels = "aeiou"

i = 0

while i < len(lines):
    decoded = []
    j = 0
    while j < len(lines[i]):
        if lines[i][j] in vowels:
            temp = lines[i][:j] + lines[i][j + 2:]
            lines[i] = temp
        j += 1
    print(lines[i])
    i += 1
