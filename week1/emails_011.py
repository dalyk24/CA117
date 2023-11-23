#!/usr/bin/env python3

import sys

def names(s):
  i = 0
  while i < len(s) and not s[i].isnumeric():
    i += 1
  return i

def format(t):
  t = t.split(".")
  i = 0
  while i < len(t):
    t[i] = t[i].capitalize()
    i += 1
  t = " ".join(t)
  return t

for line in sys.stdin.readlines():
  position = names(line)
  print(format(line[0:position]))
