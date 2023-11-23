#!/usr/bin/env python3

import sys

for line in sys.stdin:
	line = line.split()
	print (line[0].upper() in line[1].upper())
