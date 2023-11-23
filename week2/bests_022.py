#!/usr/bin/env python3

import sys

f = open(sys.argv[1], 'r')
high = 0
names = []
for line in f:
    try:
        tokens = line.strip().split()
        mark = int(tokens[0])
        name = " ".join(tokens[1:])
        if high < mark:
            high = mark
            names = [name]
        elif high == mark:
            names.append(name)
    except FileNotFoundError:
        print(f"The file {f} could not be opened.")
    except ValueError:
	    print(f"Invalid mark {tokens[0]} encountered. Skipping.")

names = ", ".join(names)

print(f"Best student(s): {names}")
print(f"Best mark: {high}")
