#!/usr/bin/env python3

import sys

lines = [l.strip().split() for l in sys.stdin.readlines()]
d = {(True, True) : 1, (True, False) : 2, (False, False) : 3, (False, True) : 4}

for l in lines:
	x, y = l
	print(d[(int(x) > 0, int(y) > 0)])
