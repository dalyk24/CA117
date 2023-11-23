#!/usr/bin/env python3

import sys

inp = sys.stdin.readlines()

def check(s):
	if "a" in s and "e" in s and "i" in s and "o" in s and "u" in s:
		return True
	return False

def countees(s):
	max = 0
	for word in s:
		if word.lower().count("e") > max:
			max = word.lower().count("e")
	mostees = [w.strip() for w in s if w.lower().count("e") == max]
	return mostees

vowels = [w.strip() for w in inp if check(w.strip().lower())]
try: 
	minv = min(vowels, key = len)
except ValueError:
	minv = "Please enter a word"
print(f"Shortest word containing all vowels: {minv}")

iary = [w.strip() for w in inp if w.strip().lower()[-4:] == "iary"]
print(f"Words ending in iary: {len(iary)}")

mostes = countees(inp)
print(f"Words with most e's: {mostes}")
