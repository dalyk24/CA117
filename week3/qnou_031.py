#!/usr/bin/env python3

import sys

inp = sys.stdin.readlines()

def checker(word):
    i = 1
    while i < len(word):
        if word[i - 1] == "q" and word[i] != "u":
            return True
        i += 1
    return False

print(f"Words with q but no u: {[s.strip() for s in inp if checker(s.lower())]}")
