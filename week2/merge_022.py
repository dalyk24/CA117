#!/usr/bin/env python3

import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1) as f1:
    nums1 = f1.readlines()

with open(file2) as f2:
    nums2 = f2.readlines()

i = 0

for num in nums1:
    print(num.strip())
    print(nums2[i].strip())
    i += 1
