#!/usr/bin/env python3

import sys

lines = [l.strip() for l in sys.stdin.readlines()]
pieces = [2, 2, 4, 4, 4, 16]

for line in lines:
    ints = line.split()
    req = []
    i = 0
    while i < len(ints):
        req.append(str(pieces[i] - int(ints[i])))
        i += 1
    print(" ".join(req))
