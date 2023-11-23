#!/usr/bin/env python3

import sys
import string

lines = sys.stdin.readlines()

def achecker(line):
	alpha = list(string.ascii_lowercase)
	line = line.strip().lower()

	for l in line:
		if l in alpha:
			alpha.remove(l)

	return alpha

for line in lines:
	pans = achecker(line)

	if pans == []:
		print("pangram")
	else:
		pans = "".join(pans)
		print(f"missing {pans}")
