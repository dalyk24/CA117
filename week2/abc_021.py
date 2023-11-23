#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
nums = lines[0].split()
i = 0

while i < len(nums):
  nums[i] = int(nums[i])
  i += 1

nums.sort()
lines[1] = lines[1].replace("A", "0")
lines[1] = lines[1].replace("B", "1")
lines[1] = lines[1].replace("C", "2")

print(nums[int(lines[1][0])], nums[int(lines[1][1])], nums[int(lines[1][2])])
