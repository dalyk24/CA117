#!/usr/bin/env python 3

import sys
import string

def unique(words):
	punctuation = string.punctuation
	for x in punctuation:
		words = words.replace(x, "")
	words = words.split()
	found = []
	for word in words:
		if word not in found:
			found.append(word)
	return len(found)

lines =  sys.stdin.read()
print(unique(lines.lower()))
