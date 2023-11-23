#!/usr/bin/env python3

import sys

def checker(s):
	i = 0
	while i < len(s[0]) and s[0][i] in s[1]:
		s[1] = s[1].replace(s[0][i], "")
		i += 1

	return i == len(s[0])

for line in sys.stdin:
	line = line.upper().strip().split()
	print(checker(line))
