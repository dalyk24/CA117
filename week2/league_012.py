#!/usr/bin/env python3

import sys

league = [["POS", "CLUB", "P", "W", "D", "L", "GF", "GA", "GD", "PTS"]]
high = 0

def findp(tokens):
  i = 0
  while i < len(tokens) and not tokens[i].isnumeric():
    i += 1
  return i + 1

for line in sys.stdin.readlines():
  currclub = []
  tokens = line.split()
  position = findp(tokens[1:])
  currclub.append(tokens[0])
  currclub.append(" ".join(tokens[1:position]))
  while position < len(tokens):
    currclub.append(tokens[position])
    position += 1
  if high < len(currclub[1]):
    high = len(currclub[1])
  league.append(currclub)

for club in league:
  print(f"{club[0]:>3s} {club[1]:{high}s} {club[2]:>2s} {club[3]:>3s} {club[4]:>3s} {club[5]:>3s} {club[6]:>3s} {club[7]:>3s} {club[8]:>3s} {club[9]:>3s}")
