#!/usr/bin/env python3

import sys

def secure(password):
	dig, low, upp, spec = False, False, False, False

	for c in password:
		if c.isnumeric():
			dig = True
		elif c.islower():
			low = True
		elif c.isupper():
			upp = True
		else:
			spec = True

	return int(dig) + int(low) + int(upp) + int(spec) 

for password in sys.stdin.readlines():
	print(secure(password.strip()))
