#!/usr/bin/env python3

import sys

calories = sys.stdin.readlines()

def calcount(c):
	if c == "0":
		return 0
      
	c = int(c)
	choccals = 400
	i = 1

	while c > choccals:
		c -= choccals
		i += 1

	return i

for c in calories:
	print(calcount(c.strip()))
