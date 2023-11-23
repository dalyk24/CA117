#!/usr/bin/env python3

import sys

def midd(s):
	s = s[len(s) // 2]
	return s

for line in sys.stdin:
	line = line.strip()
	if len(line) % 2 == 1:
		outp = midd(line)
	else:
		outp = "No middle character!"
	print(outp)
