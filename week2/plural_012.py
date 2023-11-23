#!/usr/bin/env python3

import sys

def plurals(noun):
	lower = noun.lower()
	es = ["ch", "sh", "x", "s", "z", "o"]
	cons = "bcdghjklmnpqrtvwy"

	if lower[-2:] in es or lower[-1] in es:
		return noun + "es"
	elif lower[-1]  == "y" and lower[-2] in cons:
		return noun[0:-1] + "ies"
	elif lower[-1] == "f":
		return noun[0:-1] + "ves"
	elif lower[-2:] == "fe":
		return noun[0:-2] + "ves"
	else:
		return noun + "s"

for noun in sys.stdin.readlines():
	print(plurals(noun.strip()))
