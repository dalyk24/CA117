#!/usr/bin/env python3

import sys

letters = []

for line in sys.stdin.readlines():
    line = line.strip()
    count = 1
    i = 1
    while i < len(line):
        if line[i] == line[i - 1]:
            count += 1
        else:
            letters.append(str(count) + line[i - 1])
            count = 1
        i += 1
    letters.append(str(count) + line[i - 1])
    print("".join(letters))
