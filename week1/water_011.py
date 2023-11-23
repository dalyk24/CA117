#!/usr/bin/env python3

import sys

litres = sys.stdin.readlines()

water = int(litres[0])
buckets = litres[1].split()

total = 0
count = 0
i = 0

while i < len(buckets):
  total += int(buckets[i])
  if total <= water:
    count += 1
  i += 1

print(count)
