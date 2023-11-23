#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

def lister(s):
	return s.strip().split()

for line in lines:
	unique = []
	numbers = lister(line)

	for n in numbers: 
		if numbers.count(n) == 1:
			unique.append(n)

	if unique == []:
		print("none")
	else:
		print(max(unique))
