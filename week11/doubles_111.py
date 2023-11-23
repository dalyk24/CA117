#!/usr/bin/env python3

import sys

def maxDoubles(s):
	vowels = "aeiou"
	total = 0

	for c in vowels:
		total += s.count(c*2)
	return total

words = [word.strip() for word in sys.stdin.readlines()]

wordcounts = {k : maxDoubles(k) for k in words}
print(max(wordcounts, key=lambda k: wordcounts[k]))