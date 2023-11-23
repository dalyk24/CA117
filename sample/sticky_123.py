#!/usr/bin/env python3

import sys

line1 = sys.stdin.readline().strip()
line2 = sys.stdin.readline().strip()
stickies = []

for l in line1:
    if line1.count(l) != line2.count(l):
        stickies.append(l)
        line2.replace(l, "")

setstickies = set(stickies)
outpstickies = sorted(list(setstickies))

print("".join(outpstickies))
