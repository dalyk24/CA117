#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
speeds = []
pt, pd = 0, 0

for line in lines[1:]:
	ct, cd = [int(s) for s in line.split()]
	speeds.append((cd - pd) / (ct - pt))
	pt, pd = ct, cd

print(int(max(speeds)))
