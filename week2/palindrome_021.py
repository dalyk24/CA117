#!/usr/bin/env python 3

import sys

def palin(words):
	punctuation = ".!,;:!? "
	for x in punctuation:
		words = words.replace(x, "")
	if words != words[::-1]:
		return False
	return True

for line in sys.stdin.readlines():
	print(palin(line.upper().strip()))
