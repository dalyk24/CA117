#!/usr/bin/env python3

import sys

lines = [l.strip().split() for l in sys.stdin.readlines()]

pointX = []
pointY = []

for line in lines:
    pointX.append(line[0])
    pointY.append(line[1])

for p in pointX:
    if pointX.count(p) == 1:
        sys.stdout.write(p + " ")

for p in pointY:
    if pointY.count(p) == 1:
        sys.stdout.write(p + "\n")
