#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

no_dups = []
found = []
i = 0

for line in lines:
	words = line.split()
	i = 0
	while i < len(words):
		w = [c for c in words[i] if c.isalpha() or c == "-"]
		w = "".join(w).lower()
	
		if w in found:
			words[i] = "."
		else:
			found.append(w)
		i += 1

	no_dups.append(" ".join(words))

print("\n".join(no_dups))