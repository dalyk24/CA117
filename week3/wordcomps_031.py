#!/usr/bin/env python3

import sys

inp = sys.stdin.readlines()

def letters(word, letter):
    count = 0
    for s in word:
        if s == letter:
            count += 1
    return count

def anagrams(word):
    key = "angle"
    if len(word) != len(key) or word == key:
        return False
    for s in word:
        if s not in key:
            return False
        key = key.replace(s, "")
    return True

checks = ["a", "q", "cie"]

print(f"Words containing 17 letters: {[s.strip() for s in inp if len(s.strip()) == 17]}")
print(f"Words containing 18+ letters: {[s.strip() for s in inp if len(s.strip()) >= 18]}")
print(f"Words with 4 a's: {[s.strip() for s in inp if letters(s.lower(), checks[0]) == 4]}")
print(f"Words with 2+ q's: {[s.strip() for s in inp if letters(s.lower(), checks[1]) >= 2]}")
print(f"Words containing cie: {[s.strip() for s in inp if checks[2] in s.lower()]}")
print(f"Anagrams of angle: {[s.strip() for s in inp if anagrams(s.strip().lower())]}")
