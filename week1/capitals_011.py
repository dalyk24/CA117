#!/usr/bin/env python3

import sys

def capitals(s):
	last = s[-1].capitalize()
	s = s[0:-1].capitalize()
	return s + last

for line in sys.stdin:
	capped = capitals(line.strip())
	print(capped)
