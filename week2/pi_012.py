#!/usr/bin/env python3

import sys
import math

decimals = sys.stdin.readlines()

def format(n):
  print(f"{math.pi:.{n}f}")

for num in decimals:
  format(int(num))
