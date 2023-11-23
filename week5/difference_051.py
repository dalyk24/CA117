#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
compare = []
i = 0

lines = [line.strip() for line in lines]

while i < len(lines[0]):
	if lines[0][i] == lines[1][i]:
		compare.append("-")
	else:
		compare.append("*")
	i += 1

print(lines[0])
print(lines[1])
print("".join(compare))
