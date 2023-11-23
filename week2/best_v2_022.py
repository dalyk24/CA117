#!/usr/bin/env python3

import sys

try:
    f = open(sys.argv[1], 'r')
    high = [0]
    for line in f:
        tokens = line.strip().split()
        mark = int(tokens[0])
        name = " ".join(tokens[1:])
        if high[0] < mark:
            high = [mark, name]
    print(f"Best student: {high[1]}")
    print(f"Best mark: {high[0]}")
except FileNotFoundError:
    print(f"The file {f} could not be opened.")
except ValueError:
	print(f"Invalid mark {tokens[0]} encountered. Exiting.")
