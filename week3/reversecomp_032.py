#!/usr/bin/env python3

import sys

dict = sys.stdin.readlines()

def binsearch(query, sorted_list):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] < query:
            low = mid + 1
        elif sorted_list[mid] > query:
            high = mid - 1
        else:
            return True
    return False

least5 = [w.strip() for w in dict if len(w.strip()) >= 5]
least5.sort(key=str.lower)
lowered = [w.lower() for w in least5]
pali = [w for w in least5 if binsearch(w.lower()[::-1], lowered)]
print(pali)
