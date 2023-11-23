#!/usr/bin/env python3

import sys

def findmax(lines):
    max = 0
    for line in lines:
	    if len(line) > max:
		    max = len(line)
    return max

def center(line):
    print(f"{line:^{max}s}")

lines = sys.stdin.readlines()

i = 0

while i < len(lines):
    lines[i] = lines[i].strip()
    i += 1

max = findmax(lines)

for line in lines:
    center(line)
