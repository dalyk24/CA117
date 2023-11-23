#!/usr/bin/env python 3

import sys

def anagrams(words):
	words = words.split()
	if len(words[0]) != len(words[1]):
		return False
	for letter in words[0]:
		if letter not in words[1]:
			return False
		words[1] = words[1].replace(letter, "", 1)
	return True

for line in sys.stdin.readlines():
	print(anagrams(line))
