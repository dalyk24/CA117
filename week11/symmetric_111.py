#!/usr/bin/env python3

import sys

names = [n.strip() for n in sys.stdin]
maxi = len(max(names, key=len))
limit = 0

while names != []:
    i = 0
    while i < len(names):
        if len(names[i]) > limit and len(max(names, key=len)) == maxi:
            print(names[i])
            limit = len(names[i])
            names.pop(i)
        elif len(names[i]) == len(max(names, key=len)):
    	    print(names[i])
    	    names.pop(i)
        i += 1
