#!/usr/bin/env python3

import sys
import string

stats = sys.stdin.readlines()
disqual = []
overall = {}

def tagger(line):
	return int(line[-1])

def scorecount(scores):
	try:
		sumscores = sum([int(n) for n in scores])
		return sumscores
	except ValueError:
		return "out"
        
for stat in stats:
	player = stat.strip().split()
	score = scorecount(player[-3:])
	name = " ".join(player[:-3])

	if score == "out":
		disqual.append(name)
	else:
		overall[name] = score

sortresult = sorted(overall.items(), key=tagger)

for k, v in sortresult:
	print(k + ": " + str(v))

if disqual != []:
	print("Disqualified: " + ", ".join(disqual))