#!/usr/bin/env python3

import sys

try:
    censors = sys.argv[1]
except IndexError:
    print("Please enter file in command line")
    quit()

poem = sys.stdin.readlines()

def censorer(line, censor):
    for w in censor:
        if w in line:
            line = line.replace(w, len(w) * "@")
    return line

try:
    with open(censors) as f:
        censor = f.readlines()
except FileNotFoundError:
    print("File not found")
    quit()

censor = [w.strip() for w in censor]
poem = [w.strip() for w in poem]
censored = [censorer(w, censor) for w in poem]
[print(w) for w in censored]
