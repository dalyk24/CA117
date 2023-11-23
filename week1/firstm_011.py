#!/usr/bin/env python3

import sys

for line in sys.stdin.readlines():
  sys.stdout.write(line.replace("m", "M", 1))
