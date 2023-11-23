#!/usr/bin/env python3

import sys
from re import findall

pattern = sys.stdin.readline().strip()
text = sys.stdin.read()

pattern = r'\b' + pattern.replace('-', r'\w') + r'\b'

matches = findall(pattern, text)

if matches != []:
    print(', '.join(matches))
