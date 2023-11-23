#!/usr/bin/env python3

import sys

def chop(s):
	s = s[1:-1]
	return s

for line in sys.stdin:
	chopped = chop(line.strip())
	if chopped:
		print(chopped)
